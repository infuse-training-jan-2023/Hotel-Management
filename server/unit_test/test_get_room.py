from service.room_services import RoomService




def test_get_room_makes_db_call(mocker):
  room={
     "_id": {
    "$oid": "63e68ea543eefbbf88459d29"
  },
  "room_no": 101,
  "room_type": "single",
  "price": 2000,
  "capacity": 1,
  "amenities": [
    "TV",
    "Home Theater"
  ],
  "images": [
    "download.png",
    "img1.png"
  ]
  }
  mock = mocker.patch('service.room_services.RoomService.get_room', return_value = [])
  _ = RoomService.get_room(room["room_no"])
  assert mock.call_count == 1

def test_get_room_positive(mocker):
  room={
     "_id": {
    "$oid": "63e68ea543eefbbf88459d29"
  },
  "room_no": 101,
  "room_type": "single",
  "price": 2000,
  "capacity": 1,
  "amenities": [
    "TV",
    "Home Theater"
  ],
  "images": [
    "download.png",
    "img1.png"
  ]
  }
  mock = mocker.patch('pymongo.collection.Collection.find_one', return_value = room)
  room_returned = RoomService.get_room(room["room_no"])
  print(room_returned)
  assert room == room_returned



def test_get_room_negative(mocker):
  room={
     "_id": {
    "$oid": "63e68ea543eefbbf88459d29"
  },
  "room_no": "101",
  "room_type": "single",
  "price": 2000,
  "capacity": 1,
  "amenities": [
    "TV",
    "Home Theater"
  ],
  "images": [
    "download.png",
    "img1.png"
  ]
  }
  mock = mocker.patch('pymongo.collection.Collection.find_one', return_value ={})
  room_returned = RoomService.get_room(room["room_no"]) 
  assert {} == room_returned


