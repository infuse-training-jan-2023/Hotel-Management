import sys
sys.path.insert(0, './service')
from room_services import RoomService
class RoomController:
    def get_room_details(self,room_no):
      try:
        room=RoomService.get_room(room_no)
        resp = {
          'room_no': room["room_no"],
          'room_type': room["room_type"],
          'price': room["price"],
          'capacity': room["capacity"],
          'amenities': room["amenities"],
          'images' : room["images"]
           }
        return resp
      except Exception as e:
        return str(e) 
