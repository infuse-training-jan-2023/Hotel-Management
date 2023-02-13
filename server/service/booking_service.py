import sys
sys.path.insert(0, './DB')
from connect import Connection
from service.bookings import Bookings
from bson.objectid import ObjectId
import pymongo

class BookingService:
    @staticmethod
    def book_room(request_data):
        obj =Bookings(request_data)
        record = obj.create_booking_record()
        print(record)
        try:
            result= Connection.booking.insert_one(record)
            if(result.acknowledged):
                return {"msg": "booking succesfull"}
            return {"msg": "booking failed"}
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
    
    @staticmethod
    def cancel_booking(id):
        target_booking_record = { "_id":ObjectId(id) }
        newvalues = { "$set": { "cancel_status": True } }
        try:
            updateResult= Connection.booking.update_one(target_booking_record, newvalues)
            if(updateResult.modified_count == 1):
                return {"msg" : "booking canceled"}
            return {"msg" : "booking cancellation failed "}
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
        
    @staticmethod
    def get_user_booking(customer_id):
        try:
            Result= Connection.booking.find({"customer_id":ObjectId(customer_id)})
            return Result
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)