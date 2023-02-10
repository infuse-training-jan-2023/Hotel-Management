from pymongo import MongoClient
import json
from bson import json_util

from bson.objectid import ObjectId
from connect import Connection

class Customer:
    def get_all_rooms(self):
        rooms = Connection.room.find({})
        return rooms