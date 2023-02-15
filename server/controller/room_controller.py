from service.room_services import RoomService
from flask import request

class RoomController:
    def get_room_details(self):
      try:
        room_id = request.args.get('room_id')
        room=RoomService.get_room(room_id)
        resp = {
          '_id': room["_id"],
          'room_type': room["room_type"],
          'price': room["price"],
          'capacity': room["capacity"],
          'amenities': room["amenities"],
          'images' : room["images"]
           }
        return resp
      except Exception as e:
        return str(e) 
    
    def get_all_rooms(self):
      try:
          request_data = request.get_json()
          room = RoomService.get_all_rooms(request_data)
          return room
      except Exception as e:
          return str(e)
