from pymongo import MongoClient
import json
from bson import json_util

from bson.objectid import ObjectId
from connect import Connection

class Room:
    def get_room_details(self,room_no):
        room = Connection.room.find_one({"room_no" : room_no})
        print(room)
        return room 