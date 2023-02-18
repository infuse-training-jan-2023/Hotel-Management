import pytest
from pytest_bdd import scenarios, when, then
import requests, os
from dotenv import load_dotenv

from main import app
app=app.test_client()
load_dotenv() 

scenarios('../features/get_all_add_ons.feature')

get_all_add_ons_url = os.getenv("url")+"/addons"



@when('I want to see add ons')
def get_all_add_ons():  
  pytest.api_response = app.get(get_all_add_ons_url)

@then('I should be able to see all the add ons')
def validate_response_type():
  body = pytest.api_response.get_json()
  print(body)
  for addon in body:
    assert type(addon) == dict

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def validate_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'