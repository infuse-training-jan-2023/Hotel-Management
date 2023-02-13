from service.customer_review_service import Review

data = (2,"recommended","rohan",'63e68ea543eefbbf88459d29')

def test_add_review_makes_db_call(mocker):
  mock = mocker.patch('service.customer_review_service.Review.customer_review', return_value = [])
  _ = Review.customer_review(data)
  assert mock.call_count == 1


def test_customer_review(mocker):
    mock = mocker.patch('service.customer_review_service.Review.customer_review', return_value = data)
    review_returned = Review.customer_review()
    assert data == review_returned  
