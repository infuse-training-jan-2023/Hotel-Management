from room_repository import RoomRepository
import json

class RoomAction:
  def __init__(self) -> None:
    self.room_repo = RoomRepository()


  def get_room_details(self,room_no):
    try:
      room = self.room_repo.get_room_details(room_no)
      res = {
          'room_no': room["room_no"],
          'room_type': room["room_type"],
          'price': room["price"],
          'capacity': room["capacity"],
          'amenities': room["amenities"],
          'images' : room["images"]
           }
     
     
      print(type(res))
      return res
    except Exception as e:
      print(e)
      return {}


  

