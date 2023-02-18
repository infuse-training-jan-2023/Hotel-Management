import pytest
from pytest_bdd import scenarios, when , then
import requests, os
from dotenv import load_dotenv

load_dotenv() 
import json
from main import app
app=app.test_client()

scenarios('../features/cancel_booking.feature')

cancel_booking_url = os.getenv("url")+"/booking"


data ={
    "id": "63e52044ba29b6d46527fe93"    
    }

@when('I cancel booking')
def book_room():
    pytest.api_response = app.put(cancel_booking_url, json = data)

@then('I should get confirmation message')
def validate_response_type():
    body = pytest.api_response.get_json()
    assert type(body) == dict

@then('The api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('The api Response type should be json')
def validate_content_type():
    assert pytest.api_response.headers['content-type'] == 'application/json'
