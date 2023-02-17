from DB.connect import Connection
from bson.objectid import ObjectId
import pymongo

class Review:
    @staticmethod
    def add_review(request_data):
        try:
            booking  = Connection.db.booking.find({"_id": ObjectId(request_data["booking_id"])})
            review = Connection.db.review.insert_one({"rating":int(request_data["rating"]),"feedback":request_data["feedback"],"guest_name":booking[0]["guest_name"],"room_id":ObjectId(booking[0]["room_id"])})
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
