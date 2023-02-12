from flask import Blueprint,Flask, Response, request
import json
from controller.booking_controller import BookingController

from bson.json_util import dumps
from bson import json_util

booking_bp = Blueprint('booking_bp', __name__)


@booking_bp.route('/api/book',methods=['POST'])
def book_room():
    # request_data ={
    #            "check_in":"2023/2/25",
    #            "check_out":"2023/2/26",
    #            "room_id":"63e68ea543eefbbf88459d29",
    #            "customer_id":"63e6743305e14504ac5a50e3",
    #            "add_ons":[{"service":"gym", "price":500},{"service":"break fast", "price":700}]
    #            }
    
    request_data ={
            "check_in":"2023/2/26",
            "check_out":"2023/2/28",
            "room_id":"63e68ea543eefbbf88459d29",
            "customer_id":"63e6743305e14504ac5a50e3",
            "add_ons":[{"service":"break fast", "price":200}]
            }
   
    booking_controller=BookingController()
    booking_data=booking_controller.book_room(request_data)
    print(booking_data)
    return Response(json.dumps(booking_data), mimetype='application/json', status=201)


@booking_bp.route('/api/book',methods=['PUT'])
def cancel_booking():
    id="63e52044ba29b6d46527fe93"
    booking_controller=BookingController()
    booking_data=booking_controller.cancel_booking(id)
    return Response(json.dumps(booking_data), mimetype='application/json', status=200)

@booking_bp.route('/api/book',methods=['GET'])
def get_user_booking():
    id="63e6743305e14504ac5a50e3"
    booking_controller=BookingController()
    booking_data_cursor=booking_controller.get_user_booking(id)
    booking_data = list(booking_data_cursor)
    return Response(json_util.dumps(booking_data), mimetype='application/json', status=200)