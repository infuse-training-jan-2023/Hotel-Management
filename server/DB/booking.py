from pymongo import MongoClient
import json
from bson import json_util

from bson.objectid import ObjectId
from connect import Connection

class Booking:
    def calculate_discount(self, id):
        rooms = Connection.booking.count_documents({'customer_id':ObjectId(id)})
        return rooms
    
    def add_booking(self,record):
        Connection.booking.insert_one(record)
        return 

    def cancel_booking(self,id):
        myquery = { "_id": ObjectId(id) }
        newvalues = { "$set": { "cancel_status": True } }
        Connection.booking.update_one(myquery, newvalues)
        return 
    
