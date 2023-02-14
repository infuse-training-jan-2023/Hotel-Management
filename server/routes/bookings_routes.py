from flask import Blueprint, Response
import json
from controller.booking_controller import BookingController
from bson import json_util

bookings_bp = Blueprint('bookings_bp', __name__)

@bookings_bp.route('/api/booking',methods=['POST'])
def book_room():
    booking_data=BookingController().book_room()
    return Response(json.dumps(booking_data), mimetype='application/json', status=201)

@bookings_bp.route('/api/booking',methods=['PUT'])
def cancel_booking():
    booking_data=BookingController().cancel_booking()
    return Response(json.dumps(booking_data), mimetype='application/json', status=200)

@bookings_bp.route('/api/booking',methods=['GET'])
def get_user_booking_by_id():
    booking_data=BookingController().get_user_booking_by_id()
    return Response(json_util.dumps(booking_data), mimetype='application/json', status=200)

@bookings_bp.route("/api/loyalty-discount", methods = ['GET'])
def calc_discount():
    discount = BookingController().calculate_discount(id)
    return Response(json.dumps({"discount":discount}), status=200, mimetype="application/json")