import pytest
from pytest_bdd import scenarios, when, then
import requests
scenarios('../features/get_discount.feature')

#positive
get_discount_url = "http://127.0.0.1:5000/api/loyalty-discount?id=63e670f601343886816b44c7"
@when('i am an existing customer on booking page')
def go_to_discount_api():
  pytest.api_response = requests.get(get_discount_url)

@then('i should get discount based on number of past orders')
def check_the_discount_returned():
  body = pytest.api_response.json()
  assert body['discount'] == 10

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'

#negative
get_discount_url = "http://127.0.0.1:5000/api/loyalty-discount"

@when('i am a new customer on booking page')
def go_to_discount_api():
  pytest.api_response = requests.get(get_discount_url)

@then('i should not get discount')
def check_the_discount_returned():
  body = pytest.api_response.json()
  assert body['discount'] == 0

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'