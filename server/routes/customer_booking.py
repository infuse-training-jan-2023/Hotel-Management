from flask import Blueprint, Response, request
import json
import sys
sys.path.insert(0, './controller')
from booking import BookingController

booking_bp=Blueprint('booking_bp',__name__)
@booking_bp.route("/api/loyalty-discount", methods = ['GET'])
def calc_discount():
    booking = BookingController()
    id = request.args.get('id')
    discount = booking.calculate_discount(id)
    return Response(json.dumps({"discount":discount}), status=200, mimetype="application/json")
