import sys
sys.path.insert(0, './service')
from customer_review_service import Review

class ReviewController:
    def customer_review(self,rating,feedback,name,_id):
        try:
            review = Review.customer_review(rating,feedback,name,_id)
            return review
        except Exception as e:
            return str(e)
    
    def get_all_reviews(self):
        try:
            all_reviews = Review.get_all_reviews()
            return all_reviews
        except Exception as e:
            return str(e)
            