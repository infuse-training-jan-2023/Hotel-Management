from DB.connect import Connection
from bson.objectid import ObjectId
import pymongo
from datetime import datetime

class DiscountService:
    
    @staticmethod
    def calculate_discount(customer_email):
        try:
            bookings = Connection.db.booking.count_documents({'customer_email':customer_email})
            return bookings*100
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)

   


        