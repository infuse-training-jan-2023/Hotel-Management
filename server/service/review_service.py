from DB.connect import Connection
from bson.objectid import ObjectId
import pymongo

class Review:
    @staticmethod
    def add_review(request_data):
        try:
            review = Connection.db.review.insert_one({"rating":request_data["rating"],"feedback":request_data["feedback"],"customer_name":request_data["name"],"room_id":ObjectId(request_data["room_id"])})
            return review.inserted_id
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
    
    @staticmethod
    def get_reviews_of_room(room_id):
        try:
            room  = Connection.db.room.find({"_id":ObjectId(room_id)})
            get_all_review_data = Connection.db.review.find({"room_id": ObjectId(room[0]["_id"])})
            return get_all_review_data
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
