from service.room_services import RoomService
from flask import Response,request
from bson import json_util 

class RoomController:
    def get_room_details(self):
      try:
        room_id = request.args.get('room_id')
        room=RoomService.get_room(room_id)
        room_data = {
          '_id': room["_id"],
          'title' : room["title"],
          'room_type': room["room_type"],
          'price': room["price"],
          'capacity': room["capacity"],
          'amenities': room["amenities"],
          'images' : room["images"],
          'description': room["description"]
           }
        return Response(json_util.dumps(room_data), mimetype='application/json', status=200)
      except Exception as e:
        return str(e) 
    
    def get_all_rooms(self):
      try:
          rooms = RoomService.get_all_rooms()
          return Response(json_util.dumps(rooms), status=200, mimetype="application/json")
      except Exception as e:
          return str(e)

    def get_available_rooms(self):
      try:
          request_data = request.get_json()
          rooms = RoomService.get_available_rooms(request_data)
          return Response(json_util.dumps(rooms), status=201, mimetype="application/json")
      except Exception as e:
          return str(e)