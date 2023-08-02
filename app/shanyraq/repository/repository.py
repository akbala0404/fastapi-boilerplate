
from typing import Any, List
from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult

# from ..utils.security import hash_password


class ShanyraqRepository:
    def __init__(self, database: Database):
        self.database = database
    
    # def create_user(self, user: dict):
    #     payload = {
    #         "email": user["email"],
    #         "password": hash_password(user["password"]),
    #         "created_at": datetime.utcnow(),
    #     }
    #     self.database["users"].insert_one(payload)

    def create_shanyraq(self, data: dict[str, Any]):
        shanyraq = self.database["questions"].insert_one(data)
        return shanyraq.inserted_id
    # def create_shanyraq(self, user_id: str, data: dict[str, Any]):
    #     data["user_id"] = ObjectId(user_id)
    #     shanyraq = self.database["shanyraq"].insert_one(data)
    #     return shanyraq.inserted_id
    
    def get_shanyraq(self):
        questions_collection = self.database["questions"]
        questions = list(questions_collection.find({}, {"_id": 1, "question": 1}))
        return questions
    
    def update_shanyraq(
            self, shanyraq_id: str, user_id: str, data: dict[str, Any]) -> UpdateResult:
        return self.database["shanyraq"].update_one(
            filter={"_id": ObjectId(shanyraq_id), "user_id": ObjectId(user_id)},
            update={
                "$set": data,
            },
        )

    def delete_shanyraq(self, shanyraq_id: str) -> DeleteResult:
        return self.database["questions"].delete_one(
            {"_id": ObjectId(shanyraq_id)}
        )
    
    def add_images_to_shanyraq(self, shanyraq_id: str, user_id: str, 
                               image_urls: List[str]):
        self.database["shanyraq"].update_one(
            {"_id": ObjectId(shanyraq_id), "user_id": ObjectId(user_id)},
            {"$push": {"media": {"$each": image_urls}}}
        )

    def delete_media_from_shanyraq(
            self, shanyraq_id: str, user_id: str) -> UpdateResult:
        return self.database["shanyraq"].update_one(
            {"_id": ObjectId(shanyraq_id), "user_id": ObjectId(user_id)},
            {"$unset": {"media": ""}}
        )
    