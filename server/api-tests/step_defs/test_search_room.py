import pytest
from pytest_bdd import scenarios, when, then
import requests
scenarios('../features/get_search_results.feature')

search_url = "http://127.0.0.1:5000/api/search"
data =pos_req_obj = {
    "price": "2800",
    "room_type": "penthouse",
    "check_in": "2023-02-13",
    "check_out": "2023-02-17"
}
status = [{"_id": {"$oid": "63ea04adcf0530963faef931"}, "room_no": 203, "room_type": "penthouse", "price": 8000, "capacity": 2, "amenities": ["Sea facing", "Jacuzzi", "home theatre", "room heater"], "images": ["https://images.pexels.com/photos/2635038/pexels-photo-2635038.jpeg?cs=srgb&dl=pexels-terry-magallanes-2635038.jpg&fm=jpg&w=1920&h=1282 ", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"]}]

@when('i try to search for room')
def go_to_discount_api():
  pytest.api_response = requests.post(search_url, json = data)

@then('i should get the rooms available based on filters')
def check_the_discount_returned():
  body = pytest.api_response.json()
  assert body ==status

@then('the api status code should be 201')
def check_status_code():
  assert pytest.api_response.status_code == 201

@then('the api response content type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'