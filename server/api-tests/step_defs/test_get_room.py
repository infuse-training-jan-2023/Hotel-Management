import pytest
from pytest_bdd import scenarios, when, then
import requests, os
from dotenv import load_dotenv
from main import app
app=app.test_client()
load_dotenv() 

scenarios('../features/get_room.feature')

get_room_url = os.getenv("url")+"/room?room_id=63ea04adcf0530963faef934"

@when('I select a room')
def get_room():
  pytest.api_response = app.get(get_room_url)

@then('I should get all the details of the room')
def validate_response_type():
  body = pytest.api_response.get_json()
  assert type(body) == dict

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def validate_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'