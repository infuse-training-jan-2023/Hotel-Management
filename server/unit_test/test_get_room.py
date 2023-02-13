from services.room_services import RoomService

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


def test_get_room_makes_db_call(mocker):
  mock = mocker.patch('services.room_services.RoomService.get_room', return_value = [])
  _ = RoomService.get_room(room["room_no"])
  assert mock.call_count == 1

def test_get_room(mocker):
  mock = mocker.patch('services.room_services.RoomService.get_room', return_value = room)
  room_returned = RoomService.get_room(room["room_no"])
  print(room_returned)
#   for i, item in enumerate(room_returned):
#     assert item == item[i]
  assert room == room_returned