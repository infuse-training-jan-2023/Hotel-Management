import pytest
import requests

from pytest_bdd import scenarios, when, then

scenarios('../features/get_all_review.feature')

all_review_url = "http://127.0.0.1:5000/api/reviews_of_room?room_id=63ea04adcf0530963faef934"

@when('Customer View Room')
def get_all_review():
    pytest.api_response = requests.get(all_review_url)

@then('Customer can see All Customer reviews')
def check_review_returned():
    body = pytest.api_response.json()
    for review in body:
        assert type(review) == dict

@then('Api status code should be 200')
def check_api_status():
    assert pytest.api_response.status_code == 200



