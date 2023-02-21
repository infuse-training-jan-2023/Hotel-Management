from flask import Blueprint
from controller.review_controller import ReviewController

review_bp=Blueprint('review_bp',__name__)

@review_bp.route("/review", methods = ['POST'])
def add_review():
    return ReviewController().add_review() 

@review_bp.route("/reviews/room/<string:roomId>")
def get_reviews_of_room(roomId):
    return ReviewController().get_reviews_of_room(roomId)
    