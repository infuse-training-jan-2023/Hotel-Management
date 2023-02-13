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
    def get_all_reviews():
        try:
            get_all_review_data = Connection.review.find({}, {"_id": 0, "rating": 1, "feedback": 1, "customer_name": 1})
            return get_all_review_data
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)

            # Connection.customer.insert_one({"name":"rohan","email":"rohan1258@gmail.com","phone_number":"1234567890","address":"Goa"})
        # ro =Connection.room.insert_one({"room_no":101,"room_type":"single","price":2000,"capacity":1,"amenities":["TV","Home Theater"],"images":["download.png","img1.png"]})