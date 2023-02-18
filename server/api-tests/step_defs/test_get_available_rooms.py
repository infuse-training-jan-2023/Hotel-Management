import pytest
from pytest_bdd import scenarios, when, then
import requests, os
from dotenv import load_dotenv
from main import app
app=app.test_client()
load_dotenv() 
scenarios('../features/get_available_rooms.feature')

search_url = os.getenv("url")+"/available/rooms"
data  = {
    "price": "5800",
    "check_in": "2023-04-19",
    "check_out": "2023-07-14"
}
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

@when('i try to search for rooms')
def search_room():
  pytest.api_response = app.post(search_url, json = data)

@then('i should get the rooms available based on filters')
def get_filtered_rooms():
  body = pytest.api_response.get_json()
  print(type(body))
  assert body[0]["_id"] == status[0]["_id"]

@then('the api status code should be 201')
def check_status_code():
  assert pytest.api_response.status_code == 201

@then('the api response content type should be json')
def validate_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'