from bson.objectid import ObjectId
import sys
sys.path.insert(0, './DB')
from connect import Connection
import pymongo

class Booking:
    @staticmethod
    def calculate_discount(id):
        try:
            bookings = Connection.booking.count_documents({'customer_id':ObjectId(id)})
            return bookings*10
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)

    @staticmethod
    def get_all_bookings(id):
        try:
            bookings = Connection.booking.find({"customer_id":ObjectId(id)})
            return bookings
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)