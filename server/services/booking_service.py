from db_config import Database
from model.booking import booking_schema
from services.bookings import Bookings
from bson.objectid import ObjectId
from bson import json_util


class BookingService:
    @staticmethod
    def book_room(self,request_data):
        db=Database.connect_to_db()
        collection=db["booking"]

        obj =Bookings(request_data)
        record = obj.create_booking_record()
        print(record)
        result= collection.insert_one(record)
        if(result.acknowledged):
            return {"msg": "booking succesfull"}
        return {"msg": "booking failed"}
    
    @staticmethod
    def cancel_booking(self, id):
        db=Database.connect_to_db()
        collection=db["booking"]
        target_booking_record = { "_id":ObjectId(id) }
        newvalues = { "$set": { "cancel_status": True } }
        updateResult= collection.update_one(target_booking_record, newvalues)
        if(updateResult.modified_count == 1):
            return {"msg" : "booking canceled"}
        return {"msg" : "booking cancellation failed "}
    
    @staticmethod
    def get_user_booking(self, customer_id):
        db=Database.connect_to_db()
        collection=db["booking"]
        Result= collection.find({"customer_id":ObjectId(customer_id)})
        return Result