import re
from datetime import datetime
from bson import ObjectId


def validate_fields(expected_type, value):
    """Проверяет значение по типу (email, phone, date, text)"""
    match expected_type:
        case "email":
            return re.match(r"[^@]+@[^@]+\.[^@]+", value) is not None
        case "phone":
            return re.match(r"^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$", value) is not None
        case "date":
            try:
                datetime.strptime(value, "%d.%m.%Y")
                return True
            except ValueError:
                try:
                    datetime.strptime(value, "%Y-%m-%d")
                    return True
                except ValueError:
                    return False
        case "text":
            return isinstance(value, str)
        case _:
            return False


def infer_field_types(value):
    match value:
        case _ if validate_fields("date", value):
            return "date"
        case _ if validate_fields("phone", value):
            return "phone"
        case _ if validate_fields("email", value):
            return "email"
        case _:
            return "text"


def serialize_objectid(obj):
    """Преобразует объекты ObjectId в строку для JSON-сериализации."""
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not serializable")
