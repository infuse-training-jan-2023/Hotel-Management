from src.room_repository import RoomRepository

room={
  "_id": {
    "$oid": "63e523f1964c58b41d4dc867"
  },
  "room_no": 101,
  "room_type": "penthouse",
  "price": 6000,
  "capacity": 4,
  "amenities": [
    "TV",
    "Furniture",
    "Sea facing",
    "Jacuzzi"
  ],
  "images": [
    "hall.png",
    "dining.png",
    "sea.png"
  ]
}


room_repo = RoomRepository()

def test_get_room_makes_db_call(mocker):
  mock = mocker.patch('src.room_repository.RoomRepository.get_room_details', return_value = [])
  _ = room_repo.get_room_details(room["room_no"])
  assert mock.call_count == 1

def test_get_item(mocker):
  mock = mocker.patch('src.room_repository.RoomRepository.get_room_details', return_value = room)
  room_returned = room_repo.get_room_details(room["room_no"])
  print(room_returned)
#   for i, item in enumerate(room_returned):
#     assert item == item[i]
  assert room == room_returned