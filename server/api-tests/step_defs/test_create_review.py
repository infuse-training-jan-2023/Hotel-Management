import pytest
import requests, os
from dotenv import load_dotenv

load_dotenv() 
from bson.objectid import ObjectId
from pytest_bdd import scenarios, when, then

from main import app
app=app.test_client()

scenarios('../features/create_review.feature')

create_review_url = os.getenv("url")+"/review"
data = {"booking_id": str(ObjectId('63edd7f2fb41e1fb9b50f0d0')),"rating": 4, "feedback": "good" }

@when('Customer gives a review')
def review():
    pytest.api_response = app.post(create_review_url, json=data)   

@then('Customer review should be saved to database')
def check_review_retured():
    data = pytest.api_response.get_json()
    assert isinstance(data, dict)

@then('Api status code should be 201')
def validate_api_status():
    assert pytest.api_response.status_code == 201





