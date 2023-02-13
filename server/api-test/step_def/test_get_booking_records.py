import pytest
from pytest_bdd import scenarios, when , then
import requests
import json

scenarios('../features/get_booking_records.feature')

cancel_booking_url = "http://127.0.0.1:5000/api/book"


data ={
    "customer_id": "63e52044ba29b6d46527fe93"
    }

@when('I get booking records')
def book_room():
    pytest.api_response = requests.get(cancel_booking_url, json = data)

@then('I should get list of records')
def check_the_msg_returned():
    body = pytest.api_response.json()
    assert type(body) == list

@then('The api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('The api Response type should be json')
def check_content_type():
    assert pytest.api_response.headers['content-type'] == 'application/json'
