from DB.connect import Connection
from bson.objectid import ObjectId
import pymongo
from datetime import datetime

class BookingService:

    @staticmethod
    def create_booking_record( booking_data):        
        room_price= int(booking_data.get("room_price"))
        room_cost = room_price*BookingService.get_no_of_days(booking_data)
        add_ons_cost = BookingService.get_add_ons_cost(booking_data.get("add_ons"))
        total_amount= add_ons_cost+room_cost
        return BookingService.format_booking_record(total_amount , room_price, booking_data)

    @staticmethod
    def get_no_of_days(booking_data):
        
        chk_in_date = datetime.strptime(booking_data.get("check_in"), '%Y-%m-%d')
        chk_out_date = datetime.strptime(booking_data.get("check_out"), '%Y-%m-%d')
        delta_days = chk_out_date - chk_in_date
        return 1 if delta_days.days == 0 else  delta_days.days
    
    @staticmethod
    def get_add_ons_cost( add_ons):
        addons_cost=0
        for service in add_ons:
             addons_cost += service.get("price")
        return addons_cost

    @staticmethod
    def format_booking_record( total_amount, room_price ,booking_data):
        print(f'type(booking_data.get("check_in"))   type(booking_data.get("check_out"))')
        check_in = datetime.strptime(booking_data.get("check_in"), '%Y-%m-%d')
        check_out = datetime.strptime(booking_data.get("check_out"), '%Y-%m-%d')
        add_on = booking_data.get("add_ons")
        room_id = booking_data.get("room_id")


        guest_name = booking_data.get("guest_name")
        phone_number =  booking_data.get("phone_number")
        special_request =  booking_data.get("special_request")
        customer_email = booking_data.get("customer_email")
        discount = booking_data.get("discount")
        iscancelled = False
        return {"check_in":check_in, 
                "check_out":check_out, 
                "add_ons":add_on ,
                "total_amount":total_amount-discount, 
                "room_price":room_price, 
                "customer_email":customer_email, 
                "room_id":ObjectId(room_id),
                "isCancelled":iscancelled,
                "guest_name":guest_name,
                "phone_number":phone_number,
                "special_request":special_request,
                "discount":discount}


    @staticmethod
    def book_room(request_data):
        record = BookingService.create_booking_record(request_data)
        print(record)
        try:
            result= Connection.db.booking.insert_one(record)
            if(result.acknowledged):
                return {"msg": "booking succesfull"}
            return {"msg": "booking failed"}
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
    
    @staticmethod
    def cancel_booking(booking_id):
        target_booking_record = { "_id":ObjectId(booking_id["id"]) }
        newvalues = { "$set": { "isCancelled": True } }
        try:
            updateResult= Connection.db.booking.update_one(target_booking_record, newvalues)
            if(updateResult.modified_count == 1):
                return {"msg" : "booking cancelled"}
            return {"msg" : "booking cancellation failed "}
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
        
    @staticmethod
    def get_user_booking_by_email(customer_email):
        try:
            Result= Connection.db.booking.find({"customer_email":customer_email}).sort("check_in",-1)
            return Result
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
    
    @staticmethod
    def calculate_discount(customer_email):
        try:
            bookings = Connection.db.booking.count_documents({'customer_email':customer_email})
            return bookings*100
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)

   


        