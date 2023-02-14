from DB.connect import Connection
import pymongo
from bson.objectid import ObjectId
from datetime import datetime

class RoomService:
    @staticmethod
    def get_room(room_id):
        try:
            result = Connection.db.room.find_one({"_id": ObjectId(room_id)})
            return result
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
            
