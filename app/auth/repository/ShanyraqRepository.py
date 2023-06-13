from datetime import datetime
from pymongo.database import Database
from ..adapters.jwt_service import JWTData


class ListingRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_listing(self, jwt_data: JWTData, listing_data: dict) -> str:
        user_id = jwt_data.user_id
        listing_data["user_id"] = user_id
        listing_data["created_at"] = datetime.utcnow()
        result = self.database["listings"].insert_one(listing_data)
        return str(result.inserted_id)
