from db_config import Database
from model.room import room_schema
class RoomService:
    @staticmethod
    def get_room(self,room_no):
        db=Database.connect_to_db()

        collection=db["room"]
        result= collection.find_one({"room_no": room_no})
        return result
