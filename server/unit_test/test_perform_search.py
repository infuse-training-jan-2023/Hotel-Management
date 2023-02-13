from service.search_service import Room
pos_req_obj = {
    "price": "2800",
    "room_type": "penthouse",
    "check_in": "2023-02-13",
    "check_out": "2023-02-17"
}

neg_req_obj = {
    "price": "6000",
    "room_type": "single",
    "check_in": "2023-02-13",
    "check_out": "2023-02-17"
}

pos_status = [{"_id": {"$oid": "63ea04adcf0530963faef931"}, "room_no": 203, "room_type": "penthouse", "price": 8000, "capacity": 2, "amenities": ["Sea facing", "Jacuzzi", "home theatre", "room heater"], "images": ["https://images.pexels.com/photos/2635038/pexels-photo-2635038.jpeg?cs=srgb&dl=pexels-terry-magallanes-2635038.jpg&fm=jpg&w=1920&h=1282 ", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"]}]


def test_get_search_result_positive(mocker):
  mock = mocker.patch('service.search_service.Room.get_all_rooms', return_value = pos_status)
  search_results = Room.get_all_rooms(pos_req_obj)
  print(search_results)
  assert pos_status == search_results


def test_get_search_result_negative(mocker):
  mock = mocker.patch('service.search_service.Room.get_all_rooms', return_value =[])
  search_results = Room.get_all_rooms() 
  assert [] == search_results


