import pytest
import requests
from bson.objectid import ObjectId
from pytest_bdd import scenarios, when, then

scenarios('../features/create_review.feature')

create_review_url = "http://127.0.0.1:5000/api/review"
data = {"rating": 6, "feedback": "good", "name": "rohan", "_id": str(ObjectId('63e68ea543eefbbf88459d29'))}

@when('User gives a review')
def review():
    pytest.api_response = requests.post(create_review_url, json=data)

@then('User review should be saved to database')
def check_review_retured():
    data = pytest.api_response.json()
    assert isinstance(data, dict)

@then('api api status code should be 201')
def check_api_status():
    assert pytest.api_response.status_code == 201





