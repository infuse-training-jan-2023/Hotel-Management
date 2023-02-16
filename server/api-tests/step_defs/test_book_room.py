import pytest
from pytest_bdd import scenarios, when , then
import requests

scenarios('../features/book_room.feature')

book_room_url = "http://127.0.0.1:5000/api/booking"


data = {
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
    pytest.api_response = requests.post(book_room_url , json = data)

@then('I should get confirmation message')
def check_the_msg_returned():
    body = pytest.api_response.json()
    assert type(body) == dict

@then('The api status code should be 201')
def check_status_code():
    assert pytest.api_response.status_code == 201

@then('The api Response type should be json')
def check_content_type():
    assert pytest.api_response.headers['content-type'] == 'application/json'
