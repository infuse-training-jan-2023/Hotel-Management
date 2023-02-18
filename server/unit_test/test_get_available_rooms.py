from service.room_services import RoomService

status = [
	{
		"_id": {
			"$oid": "63ea04adcf0530963faef931"
		},
		"room_no": 203,
		"room_type": "penthouse",
		"price": 8000,
		"capacity": 2,
		"amenities": [
			"jacuzzi",
			"wine",
			"speaker",
			"tv",
			"ac"
		],
		"images": [
			"https://images.pexels.com/photos/4915547/pexels-photo-4915547.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
			"https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281",
			"https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"
		],
		"description": "At 5,000 square feet, this penthouse suite at the new view, a Luxury Collection Hotel, in Milan is the largest suite in India and it may also be the country's most sumptuous with glitzy Art Deco-inspired décor and precious materials like marble and crystal gracing nearly every surface. The white and gold living room with slanted reflecting walls features some of the most iconic Italian furnishings like mushroom-shaped Atollo table lamps, and brilliant white Chesterfield sofas by Fendi.",
		"title": "A grand space for a lavish stay at this Penthouse"
	}
]

def test_get_available_rooms_makes_db_call(mocker):
  mock = mocker.patch('service.room_services.RoomService.get_available_rooms', return_value = [])
  _ = RoomService.get_available_rooms()
  assert mock.call_count == 1

def test_get_all_rooms(mocker):
  mocker.patch('service.room_services.RoomService.get_available_rooms', return_value = status)
  rooms_returned = RoomService.get_all_rooms()
  assert status == rooms_returned

