from model.room import Room
from services.room_services import RoomService
class RoomController:
    def get_room_details(self,room_no):
        room=RoomService.get_room(self,room_no)
        resp = {
          'room_no': room["room_no"],
          'room_type': room["room_type"],
          'price': room["price"],
          'capacity': room["capacity"],
          'amenities': room["amenities"],
          'images' : room["images"]
           }
        return resp
