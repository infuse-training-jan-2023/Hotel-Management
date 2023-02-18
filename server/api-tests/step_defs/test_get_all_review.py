import pytest
import requests, os
from dotenv import load_dotenv

load_dotenv() 

from pytest_bdd import scenarios, when, then
from main import app
app=app.test_client()
scenarios('../features/get_all_review.feature')

all_review_url = os.getenv("url")+"/reviews/room/63ea04adcf0530963faef934"

@when('Customer View Room')
def get_all_review():
    pytest.api_response = app.get(all_review_url)

@then('Customer can see All Customer reviews')
def validate_response_type_for_review():
    body = pytest.api_response.get_json()
    for review in body:
        assert type(review) == dict

@then('Api status code should be 200')
def check_api_status():
    assert pytest.api_response.status_code == 200



