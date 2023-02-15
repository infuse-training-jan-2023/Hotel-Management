from service.review_service import Review
from flask import request
class ReviewController:
    def add_review(self):
        try:
            request_data = request.get_json()
            review = Review.add_review(request_data)
            return review
        except Exception as e:
            return str(e)
    
    def get_reviews_of_room(self):
        try:
            room_id =request.args.get('room_id')
            all_reviews = Review.get_reviews_of_room(room_id)
            return all_reviews
        except Exception as e:
            return str(e)
            