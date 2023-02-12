from model.booking import booking_schema
from services.booking_service import BookingService
class BookingController:
    def book_room(self,request_data):
        DB_operation_status=BookingService.book_room(self,request_data)
        return DB_operation_status
  
    def cancel_booking(self , id):
          DB_operation_status=BookingService.cancel_booking(self,id)
          return DB_operation_status
    
    def get_user_booking(self ,customer_id):
          DB_operation_result=BookingService.get_user_booking(self,customer_id)
          return DB_operation_result