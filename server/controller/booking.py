import sys
sys.path.insert(0, './service')
from customer_booking_service import Booking

class BookingController:
    def calculate_discount(self,id):
        try:
            booking = Booking.calculate_discount(id)
            return booking
        except Exception as e:
            return str(e)
    
    def get_all_bookings(self,id):
        try:
            booking = Booking.get_all_bookings(id)
            return booking
        except Exception as e:
            return str(e)