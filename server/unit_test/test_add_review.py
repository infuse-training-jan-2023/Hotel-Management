import sys
sys.path.insert(0, './service')
from bson.objectid import ObjectId
from customer_review_service import Review

data = {"rating":2,"feedback":"recommended","name":"rohan","_id":ObjectId('63e68ea543eefbbf88459d29')}

def test_add_review_makes_db_call(mocker):

  mock = mocker.patch('customer_review_service.Review.customer_review', return_value = [])
  _ = Review.customer_review(data)
  assert mock.call_count == 1


def test_customer_review(mocker):
    mock = mocker.patch('services.customer_review_service.Review.customer_review', return_value = result)
    msg_returned = Review.customer_review()
    assert result == msg_returned  