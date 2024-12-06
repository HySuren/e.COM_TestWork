from fastapi import FastAPI, Request
from bson import ObjectId
from app.utils import validate_fields, infer_field_types
from app.config import templates
from app.db.mongodb import mongodb
from app.logger import logger

from descriptions.description import *
import json

app = FastAPI()



@app.on_event("startup")
async def startup_event():
    await mongodb.connect()

    form_templates_collection = mongodb.get_collection("form_templates")

    if "form_templates" not in await mongodb.db.list_collection_names():
        logger.info("Коллекция form_templates не найдена, создаем и заполняем её.")
        try:
            await form_templates_collection.insert_many(templates)
            logger.info(f"Шаблоны загружены в коллекцию 'form_templates'.")
        except FileNotFoundError:
            logger.error(f"Файл с шаблонами не найден: {template_file_path}")
        except json.JSONDecodeError:
            logger.error(f"Ошибка при декодировании JSON в файле: {template_file_path}")

    else:
        logger.info("Коллекция form_templates уже существует.")

    @app.on_event("shutdown")
    async def shutdown_event():
        await mongodb.disconnect()
        logger.info("Соединение с MongoDB закрыто.")


@app.post("/get_form", description=GET_FORM_DESCRIPTION)
async def get_form(request: Request):
    form_data = await request.json()

    form_templates_collection = mongodb.get_collection("form_templates")
    form_templates = await form_templates_collection.find().to_list(100)

    validation_errors = {}

    for template in form_templates:
        template_fields = {key: value for key, value in template.items() if key != "_id" and key != "name"}

        missing_fields = [
            field for field in template_fields if field not in form_data
        ]

        if missing_fields:
            continue

        is_valid = True
        for field in template_fields:
            field_value = form_data.get(field)
            expected_type = template_fields[field]

            if not validate_fields(expected_type, field_value):
                validation_errors[field] = f"Invalid value for {field}: {field_value} should be {expected_type}"
                is_valid = False

        if is_valid:
            return {"template_name": template["name"]}

    inferred_types = {key: infer_field_types(value) for key, value in form_data.items()}
    return inferred_types
