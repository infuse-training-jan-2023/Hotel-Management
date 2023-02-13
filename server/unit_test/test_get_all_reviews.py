from service.customer_review_service import Review
data =[
  {
    "_id": "63e8ca3cca927fb2db4457f7",
    "rating": 2,
    "feedback": "recommended",
    "customer_name": "rohan",
    "room_id": "63e68ea543eefbbf88459d29"
  },
  {
    "_id": "63e8d08f31ea08a9ff8798e3",
    "rating": 2,
    "feedback": "recommended",
    "customer_name": "rohan",
    "room_id": "63e68ea543eefbbf88459d29"
  }
  ]

def test_get_all_reviews_makes_db_call(mocker):
  mock = mocker.patch('service.customer_review_service.Review.get_all_reviews', return_value = [])
  _ = Review.get_all_reviews()
  assert mock.call_count == 1


def test_get_all_reviews(mocker):
    mock = mocker.patch('service.customer_review_service.Review.get_all_reviews', return_value = data)
    review_returned = Review.get_all_reviews()
    for i, review in enumerate(review_returned):
      assert review == data[i]
