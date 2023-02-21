from service.review_service import Review

data = (2,"recommended","rohan",'63e68ea543eefbbf88459d29')

def test_add_review_makes_db_call(mocker):
  mock = mocker.patch('service.review_service.Review.add_review', return_value = [])
  _ = Review.add_review(data)
  assert mock.call_count == 1


def test_customer_review(mocker):
    mocker.patch('service.review_service.Review.add_review', return_value = data)
    review_returned_id = Review.add_review()
    assert data[0]==review_returned_id[0]
