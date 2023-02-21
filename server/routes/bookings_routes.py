from flask import Blueprint 
from controller.booking_controller import BookingController

bookings_bp = Blueprint('bookings_bp', __name__)

@bookings_bp.route('/booking',methods=['POST'])
def book_room():
    return BookingController().book_room()

@bookings_bp.route('/booking',methods=['PUT'])
def cancel_booking():
    return BookingController().cancel_booking()

@bookings_bp.route('/booking',methods=['GET'])
def get_user_booking_by_email():
    return BookingController().get_user_booking_by_email()
    
@bookings_bp.route("/loyalty-discount", methods = ['GET'])
def calc_discount():
   return BookingController().calculate_discount()
    