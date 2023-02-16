import pytest
from pytest_bdd import scenarios, when , then
import requests
import json

scenarios('../features/get_booking_records.feature')

cancel_booking_url = "http://127.0.0.1:5000/api/booking"


data ={
    "customer_email": "bob@gmail.com"
    }

@when('I select on profile')
def book_room():
    pytest.api_response = requests.get(cancel_booking_url, json = data)

@then('I should get list of booking records')
def check_the_msg_returned():
    body = pytest.api_response.json()
    assert type(body) == list

@then('the api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('the api response type should be json')
def check_content_type():
    assert pytest.api_response.headers['content-type'] == 'application/json'
