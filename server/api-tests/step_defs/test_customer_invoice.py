import pytest
import requests
from io import BytesIO
import pypdf
from pytest_bdd import scenarios, when, then

scenarios('../features/customer_invoice.feature')

get_invoice = "http://127.0.0.1:5000/api/invoice?id=63ee1df084568668124971f6"

@when('Customer click Download Invoice')
def get_customer_response():
    pytest.api_response = requests.get(get_invoice)

@then('Customer can see Invoice')
def check_pdf_returned():
    pdf_reader = pypdf.PdfReader(BytesIO(pytest.api_response.content))
    assert len(pdf_reader.pages) == 1

@then('Api status code should be 200')
def check_api_status():
    assert pytest.api_response.status_code == 200

@then('Api response content type should be application/pdf')
def check_api_content_type():
    assert pytest.api_response.headers['content-Type'] == 'application/pdf'

