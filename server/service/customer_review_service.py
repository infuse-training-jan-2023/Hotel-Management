import sys
sys.path.insert(0, './DB')
from connect import Connection
from bson.objectid import ObjectId
import pymongo

class Review:
    @staticmethod
    def customer_review(rating,feedback,name,_id):
        try:
            customer_name = Connection.customer.find_one({"name":name})
            room_id  = Connection.room.find_one(ObjectId(_id))
            review = Connection.review.insert_one({"rating":rating,"feedback":feedback,"customer_name":customer_name.get("name"),"room_id":room_id.get("_id")})
            return review.inserted_id
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
    
    @staticmethod
    def get_all_reviews(_id):
        try:
            room  = Connection.room.find({"_id":ObjectId(_id)})
            get_all_review_data = Connection.review.find({"room_id": ObjectId(room[0]["_id"])})
            return get_all_review_data
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
