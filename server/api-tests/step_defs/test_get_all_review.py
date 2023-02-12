import pytest
import requests

from pytest_bdd import scenarios, when, then

scenarios('../features/get_all_review.feature')

all_review = "http://127.0.0.1:5000/api/get_all_review"

@when('Customer View Room')
def get_all_review():
    pytest.api_response = requests.get(all_review)

@then('Customer can see All Customer reviews')
def check_review_returned():
    body = pytest.api_response.json()
    for review in body:
        assert type(review) == dict

@then('Api status code should be 200')
def check_api_status():
    assert pytest.api_response.status_code == 200



