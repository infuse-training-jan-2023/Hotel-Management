from service.booking_service import BookingService
from flask import request
class BookingController:
    def book_room(self):
        try:
            request_data = request.get_json()
            DB_operation_status=BookingService.book_room(request_data)
            return DB_operation_status
        except Exception as e:
            return str(e)
  
    def cancel_booking(self):
        try:
            booking_id = request.get_json()
            DB_operation_status=BookingService.cancel_booking(booking_id)
            return DB_operation_status
        except Exception as e:
            return str(e)   
    
    def get_user_booking_by_email(self):
        try:
            customer_email = request.args.get('customer_email')
            DB_operation_result=BookingService.get_user_booking_by_email(customer_email)
            return DB_operation_result
        except Exception as e:
            return str(e)
    
    def calculate_discount(self):
        try:
            customer_email = request.args.get('customer_email')
            booking = BookingService.calculate_discount(customer_email)
            return booking
        except Exception as e:
            return str(e)