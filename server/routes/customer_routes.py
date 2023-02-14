from flask import Blueprint, Response
from bson import json_util
from controller.customer_controller import CustomerController

customer_bp=Blueprint('customer_bp',__name__)
@customer_bp.route("/api/user", methods = ['GET'])
def customer_details():
    customer_data = CustomerController.get_customer_details()       
    return Response(json_util.dumps(customer_data), status=201, mimetype="application/json")
