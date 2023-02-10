from pymongo import MongoClient
import json
from bson import json_util

from bson.objectid import ObjectId
from connect import Connection

class Booking:
    def calculate_discount(self, id):
        rooms = Connection.booking.count_documents({'customer_id':ObjectId(id)})
        return rooms