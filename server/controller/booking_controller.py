import sys
sys.path.insert(0, './service')
from booking_service import BookingService

class BookingController:
    def book_room(self,request_data):
        try:
            DB_operation_status=BookingService.book_room(request_data)
            return DB_operation_status
        except Exception as e:
            return str(e)
  
    def cancel_booking(self , id):
        try:
            DB_operation_status=BookingService.cancel_booking(id)
            return DB_operation_status
        except Exception as e:
            return str(e)   
    
    def get_user_booking(self ,customer_id):
        try:
            DB_operation_result=BookingService.get_user_booking(customer_id)
            return DB_operation_result
        except Exception as e:
            return str(e)