import sys
sys.path.insert(0, './service')

from customer_review_service import Review

class ReviewController:
    def customer_review(self,data):
        try:
            review = Review.customer_review(self,data)
            return review
        except Exception as e:
            return str(e)