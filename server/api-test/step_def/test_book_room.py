import pytest
from pytest_bdd import scenarios, when , then
import requests
import json

scenarios('../features/book_room.feature')

book_room_url = "http://127.0.0.1:5000/api/book"


data ={
        "check_in":"2023/2/26",
        "check_out":"2023/2/28",
        "room_id":"63e68ea543eefbbf88459d29",
        "customer_id":"63e6743305e14504ac5a50e3",
        "add_ons":[{"service":"break fast", "price":200}]
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
