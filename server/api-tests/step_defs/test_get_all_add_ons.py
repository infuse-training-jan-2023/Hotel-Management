import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/get_all_add_ons.feature')

get_all_add_ons_url = "http://127.0.0.1:5000/api/add-ons"

@when('I want to see add ons')
def get_all_add_ons():
  pytest.api_response = requests.get(get_all_add_ons_url)

@then('I should be able to see all the add ons')
def check_the_addons_returned():
  body = pytest.api_response.json()
  for addon in body:
    assert type(addon) == dict

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def check_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'