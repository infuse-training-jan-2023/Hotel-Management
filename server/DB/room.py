from pymongo import MongoClient
import json
from bson import json_util

from bson.objectid import ObjectId
from connect import Connection


class Room:
    def get_room_price(self, id):
        room = Connection.room.find_one({'_id':ObjectId(id)})
        return room.get("price")