import pytest
from pytest_bdd import scenarios, when , then
import requests, os
from dotenv import load_dotenv
load_dotenv() 

from main import app
app=app.test_client()


scenarios('../features/book_room.feature')

book_room_url = os.getenv("url")+"/booking"


dummy_booking_data = {
    "check_in":"2023-2-26",
    "check_out":"2023-2-28",
    "add_ons":[{"name":"Breakfast", "price":200}],
    "total_amount" : 2600,
    "room_price" : 2000,
    "customer_email": "user@gmail.com",
    "room_id":"63e68ea543eefbbf88459d29",
    "isCancelled": False,
    "guest_name" : "tommy",
    "phone_number" :"1234567890",
    "special_request" : "none",
    "discount" : 0
}

@when('I book a room')
def book_room():
    pytest.api_response = app.post(book_room_url , json = dummy_booking_data)

@then('I should get confirmation message')
def validate_response_type():
    body = pytest.api_response.get_json()
    assert type(body) == dict

@then('The api status code should be 201')
def check_status_code():
    assert pytest.api_response.status_code == 201

@then('The api Response type should be json')
def validate_content_type():
    assert pytest.api_response.headers['content-type'] == 'application/json'
