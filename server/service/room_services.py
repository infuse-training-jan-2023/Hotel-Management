import sys
sys.path.insert(0, './DB')
from connect import Connection
import pymongo
from bson.objectid import ObjectId
class RoomService:
    @staticmethod
    def get_room(room_id):
        try:
<<<<<<< HEAD
            result = Connection.room.find_one({"_id": ObjectId(room_id)})
=======
            result = Connection.room.find_one({"room_no": room_no})
            
>>>>>>> 92317075330f93633f5a7f91acee2ed6e2a05876
            return result
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
