from src.database import MongoDBConnection
from bson import ObjectId


class UserService:
    def __init__(self):
        self.collection = MongoDBConnection().get_collection('users')

    def create_user(self, user_data):
        result = self.collection.insert_one(user_data)
        return str(result.inserted_id)

    def get_user(self, user_id):
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return user if user else None

    def update_user(self, user_id, updated_data):
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": updated_data}
        )
        return result.modified_count > 0

    def delete_user(self, user_id):
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
