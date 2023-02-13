import sys
sys.path.insert(0, './DB')
from connect import Connection
import pymongo

class RoomService:
    @staticmethod
    def get_room(room_no):
        try:
            result = Connection.room.find_one({"room_no": room_no})
            return result
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
