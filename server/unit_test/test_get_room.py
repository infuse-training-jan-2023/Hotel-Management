from service.room_services import RoomService
import pymongo
from bson.objectid import ObjectId
room={
  "_id": {
    "$oid": "63ea04adcf0530963faef92e"
  },
  "room_no": 102,
  "room_type": "double",
  "price": 3000,
  "capacity": 3,
  "amenities": [
    "couch",
    "jacuzzi"
  ],
  "images": [
    "https://images.pexels.com/photos/1743231/pexels-photo-1743231.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281",
    "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"
  ],
  "description": "Additional space to unwind in after a tiring day of attending to business. The deluxe rooms are fitted with twin beds and gives you a few extra sq. feet to just stretch yourself and relax."
}

def test_get_room_makes_db_call(mocker):

  mock = mocker.patch('service.room_services.RoomService.get_room', return_value = [])
  _ = RoomService.get_room(ObjectId(room["_id"]["$oid"]))
  assert mock.call_count == 1


def test_get_room_positive(mocker):

  mocker.patch('service.room_services.RoomService.get_room', return_value = room)
  room_returned = RoomService.get_room(ObjectId(room["_id"]["$oid"]))
  print(room_returned)
  assert room == room_returned

def test_get_room_negative(mocker):
  id="63ea04adcf0530963faef92f"
  mock = mocker.patch('service.room_services.RoomService.get_room', return_value ={})
  room_returned = RoomService.get_room(id) 
  assert {} == room_returned

# def test_get_room_positive(mocker):

#   mocker.patch('pymongo.collection.Collection.find_one', return_value = room)
#   room_returned = RoomService.get_room(ObjectId(room["_id"]["$oid"]))
#   print(room_returned)
#   assert room == room_returned

# def test_get_room_negative(mocker):
#   id="63ea04adcf0530963faef92f"
#   mock = mocker.patch('pymongo.collection.Collection.find_one', return_value ={})
#   room_returned = RoomService.get_room(id) 
#   assert {} == room_returned


