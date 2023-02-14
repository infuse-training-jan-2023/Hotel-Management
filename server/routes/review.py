from flask import Blueprint, Response
from bson import json_util
from controller.review_controller import ReviewController

review_bp=Blueprint('review_bp',__name__)
@review_bp.route("/api/review", methods = ['POST'])
def add_review():
    review = ReviewController().add_review() 
    return Response(json_util.dumps(review), status=201, mimetype="application/json")

@review_bp.route("/api/reviews_of_room", methods = ['GET'])
def get_reviews_of_room():
    review = ReviewController().get_reviews_of_room()
    return Response(json_util.dumps(review), status=200, mimetype="application/json")