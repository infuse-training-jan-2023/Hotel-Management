import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/get_booking_records.feature')

get_customer_url = "http://127.0.0.1:5000/api/booking?email=bob@gmail.com"

@when('I select on profile')
def get_customer():
  pytest.api_response = requests.get(get_customer_url)

@then('I should get list of booking records')
def check_the_customer_returned():
  body = pytest.api_response.json()
  # for room in body:
  #   assert type(room) == str
  assert type(body) == list

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'