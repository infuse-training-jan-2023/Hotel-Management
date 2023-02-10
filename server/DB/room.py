import json
from bson import json_util
from booking import Booking

from connect import Connection

class Room:
    def get_all_rooms(self, filters):
        #print(filters)
        rooms = Connection.room.find(filters)
        return rooms
