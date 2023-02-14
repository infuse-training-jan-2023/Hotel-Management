from flask import Blueprint, Response, request
from bson.objectid import ObjectId
import sys
sys.path.insert(0, './controller')
from bson import json_util
from  customer_controller import CustomerController

customer_bp=Blueprint('customer_bp',__name__)
@customer_bp.route("/user", methods = ['GET'])
def customer_details():
    email = request.args.get('email')
    print(email)
    customer_data = CustomerController.get_customer_details(email)       
    return Response(json_util.dumps(customer_data), status=201, mimetype="application/json")
