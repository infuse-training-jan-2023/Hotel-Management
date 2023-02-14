from flask import Blueprint, Response,request
from bson.objectid import ObjectId
import sys
sys.path.insert(0, './controller')
from bson import json_util
from review import ReviewController

review_bp=Blueprint('review_bp',__name__)
@review_bp.route("/review", methods = ['POST'])
def customer_review():
    review = ReviewController()
    request_data = request.get_json()
    rating = request_data.get('rating')
    feedback = request_data.get('feedback')
    name = request_data.get('name')
    _id = request_data.get('_id')
    customer = review.customer_review(rating,feedback,name,_id)        
    return Response(json_util.dumps(customer), status=201, mimetype="application/json")

@review_bp.route("/get_all_review", methods = ['GET'])
def get_all_review():
    review = ReviewController()
    _id =request.args.get('_id')
    all_review = review.get_all_reviews(_id)
    return Response(json_util.dumps(all_review), status=200, mimetype="application/json")