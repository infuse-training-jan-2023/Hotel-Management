import json
from bson.objectid import ObjectId
from connect import Connection

class Booking:
    def calculate_discount(self, id):
        bookings = Connection.booking.count_documents({'customer_id':ObjectId(id)})
        return bookings*10

    def get_all_bookings(self):
        bookings = Connection.booking.find({})
        return bookings

