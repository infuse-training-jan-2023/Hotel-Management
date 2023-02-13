import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/get_customer.feature')

get_customer_url = "http://127.0.0.1:5000/api/user/bob@gmail.com"

@when('customer wants to see profile')
def get_customer():
  pytest.api_response = requests.get(get_customer_url)

@then('customer should be able to see details')
def check_the_customer_returned():
  body = pytest.api_response.json()
  # for room in body:
  #   assert type(room) == str
  assert type(body) == dict

@then('the api status code should be 201')
def check_status_code():
  assert pytest.api_response.status_code == 201

@then('the api response content type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'