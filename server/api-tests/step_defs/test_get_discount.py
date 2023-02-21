import pytest
from pytest_bdd import scenarios, when, then
import requests, os
from dotenv import load_dotenv
from main import app
app=app.test_client()
load_dotenv() 
scenarios('../features/get_discount.feature')

#positive
get_discount_url = os.getenv("url")+"/loyalty-discount?email=bob@gmail.com"
@when('i am an existing customer on booking page')
def go_to_discount_api():
  pytest.api_response = app.get(get_discount_url)

@then('i should get discount based on number of past orders')
def check_the_discount_returned():
  body = pytest.api_response.get_json()
  assert body['discount'] == 0

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'

#negative
get_discount_url = os.getenv("url")+"/loyalty-discount"

@when('i am a new customer on booking page')
def go_to_discount_api():
  pytest.api_response = app.get(get_discount_url)

@then('i should not get discount')
def check_the_discount_returned():
  body = pytest.api_response.get_json()
  assert body['discount'] == 0

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def validate_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'