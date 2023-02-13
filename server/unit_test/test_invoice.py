from service.invoice_service import Invoice

data = '63ea0a2a75a84883f4662ee0'

def test_invoice_review(mocker):
    mock = mocker.patch('service.invoice_service.Invoice.get_invoice', return_value = data)
    review_returned = Invoice.get_invoice()
    assert data == review_returned  

def test_invoice_review_makes_db_call(mocker):
  mock = mocker.patch('service.invoice_service.Invoice.get_invoice', return_value = [])
  _ = Invoice.get_invoice()
  assert mock.call_count == 1