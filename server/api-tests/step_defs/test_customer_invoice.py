import pytest
import requests, os
from dotenv import load_dotenv

load_dotenv() 
from io import BytesIO
import pypdf
from pytest_bdd import scenarios, when, then
from main import app
app=app.test_client()

scenarios('../features/customer_invoice.feature')

get_invoice = os.getenv("url")+"/invoice?id=63edd7f2fb41e1fb9b50f0d0"

@when('Customer click Download Invoice')
def get_customer_response():
    pytest.api_response = app.get(get_invoice)

@then('Customer can see Invoice')
def check_pdf_returned():
  
    pdf_reader = pypdf.PdfReader(BytesIO(pytest.api_response.data))
    assert len(pdf_reader.pages) == 1

@then('Api status code should be 200')
def check_api_status():
    assert pytest.api_response.status_code == 200

@then('Api response content type should be application/pdf')
def validate_api_content_type():
    assert pytest.api_response.headers['content-Type'] == 'application/pdf'

