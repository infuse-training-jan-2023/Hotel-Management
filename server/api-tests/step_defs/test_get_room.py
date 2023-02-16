import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/get_room.feature')

get_room_url = "http://127.0.0.1:5000/api/rooms?room_id=63ea04adcf0530963faef934"

@when('I select a room')
def get_room():
  pytest.api_response = requests.get(get_room_url)

@then('I should get all the details of the room')
def check_the_room_returned():
  body = pytest.api_response.json()
  # for room in body:
  #   assert type(room) == str
  assert type(body) == dict

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'