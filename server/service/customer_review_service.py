import sys
sys.path.insert(0, './DB')
from connect import Connection
class Review:
    def customer_review(self,data):
        try:
            customer_name = Connection.customer.find_one({"name":data["name"]})
            room_id  = Connection.room.find_one(data["_id"])
            review = Connection.review.insert_one({"rating":data["rating"],"feedback":data["feedback"],"customer_name":customer_name.get("name"),"room_id":room_id.get("_id")})
            return review.inserted_id
        except Exception as e:
            raise Exception("Error:", e.__class__)

            # Connection.customer.insert_one({"name":"rohan","email":"rohan1258@gmail.com","phone_number":"1234567890","address":"Goa"})
        # ro =Connection.room.insert_one({"room_no":101,"room_type":"single","price":2000,"capacity":1,"amenities":["TV","Home Theater"],"images":["download.png","img1.png"]})