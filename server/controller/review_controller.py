from service.review_service import Review
from flask import Response,request
from bson import json_util
class ReviewController:
    def add_review(self):
        try:
            request_data = request.get_json()
            review = Review.add_review(request_data)
            return Response(json_util.dumps(review), status=201, mimetype="application/json")
        except Exception as e:
            return str(e)
    
    def get_reviews_of_room(self, roomId):
        try:
            all_reviews = Review.get_reviews_of_room(roomId)
            return Response(json_util.dumps(all_reviews), status=200, mimetype="application/json")
        except Exception as e:
            return str(e)
            