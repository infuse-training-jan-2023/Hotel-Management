import pytest
from pytest_bdd import scenarios, when , then
import requests, os
from dotenv import load_dotenv

load_dotenv() 
import json
from main import app
app=app.test_client()
scenarios('../features/get_booking_records.feature')

cancel_booking_url = os.getenv("url")+"/booking"


data ={
    "customer_email": "bob@gmail.com"
    }

@when('I select on profile')
def book_room():
    pytest.api_response = app.get(cancel_booking_url, json = data)

@then('I should get list of booking records')
def validate_response_type():
    body = pytest.api_response.get_json()
    assert type(body) == list

@then('the api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('the api response type should be json')
def validate_content_type():
    assert pytest.api_response.headers['content-type'] == 'application/json'
