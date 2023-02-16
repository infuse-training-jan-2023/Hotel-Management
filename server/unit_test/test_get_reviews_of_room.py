from service.review_service import Review
data =[
  {
    "_id": "63e8ca3cca927fb2db4457f7",
    "rating": 2,
    "feedback": "recommended",
    "guest_name": "rohan",
    "room_id": "63e68ea543eefbbf88459d29"
  },
  {
    "_id": "63e8d08f31ea08a9ff8798e3",
    "rating": 2,
    "feedback": "recommended",
    "guest_name": "rohan",
    "room_id": "63e68ea543eefbbf88459d29"
  }
  ]
room_id="63e68ea543eefbbf88459d29"
def test_get_all_reviews_makes_db_call(mocker):
  mock = mocker.patch('service.review_service.Review.get_reviews_of_room', return_value = [])
  _ = Review.get_reviews_of_room()
  assert mock.call_count == 1


def test_get_reviews_of_a_room(mocker):
    mocker.patch('service.review_service.Review.get_reviews_of_room', return_value = data)
    review_returned = Review.get_reviews_of_room(room_id)
    for i, review in enumerate(review_returned):
      assert review == data[i]
