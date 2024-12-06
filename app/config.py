from dotenv import load_dotenv
import os
import json

load_dotenv()

class MongoDbConfig:
    HOST = os.getenv("MONGO_HOST")
    PORT = int(os.getenv("MONGO_PORT", 27017))
    DB_NAME = os.getenv("MONGO_DB_NAME")

    @classmethod
    def get_connection_uri(cls):
        return f"mongodb://{cls.HOST}:{cls.PORT}/{cls.DB_NAME}"


class TeamplatesConfig:
    TEMPLATES_FILE = os.path.join(os.path.dirname(__file__), "templates.json")

    @classmethod
    def load_templates(cls):
        with open(cls.TEMPLATES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

print(MongoDbConfig.DB_NAME)
template = TeamplatesConfig()
templates = template.load_templates()
