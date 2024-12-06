from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MongoDbConfig


class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(MongoDbConfig.get_connection_uri())
        self.db = self.client[MongoDbConfig.DB_NAME]
        print("MongoDB connected")

    async def disconnect(self):
        if self.client:
            self.client.close()
            print("MongoDB disconnected")

    def get_collection(self, collection_name: str):
        if self.db is None:
            raise Exception("MongoDB не подключен.")
        return self.db[collection_name]


mongodb = MongoDB()
