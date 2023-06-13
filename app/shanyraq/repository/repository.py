# from datetime import datetime
from typing import Any
from bson.objectid import ObjectId
from pymongo.database import Database

# from ..utils.security import hash_password


class ShanyraqRepository:
    def __init__(self, database: Database):
        self.database = database
    
    def create_shanyraq(self, user_id: str, data: dict[str, Any]):
        data["user_id"] = ObjectId(user_id)
        shanyraq = self.database["users"].insert_one(data)
        return shanyraq.inserted_id