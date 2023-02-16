import pytest
import requests
from bson.objectid import ObjectId
from pytest_bdd import scenarios, when, then

scenarios('../features/create_review.feature')

create_review_url = "http://127.0.0.1:5000/api/review"
data = {"booking_id": str(ObjectId('63ee1df084568668124971f6')),"rating": 6, "feedback": "good" }

@when('Customer gives a review')
def review():
    pytest.api_response = requests.post(create_review_url, json=data)   

@then('Customer review should be saved to database')
def check_review_retured():
    data = pytest.api_response.json()
    assert isinstance(data, dict)

@then('Api status code should be 201')
def check_api_status():
    assert pytest.api_response.status_code == 201





