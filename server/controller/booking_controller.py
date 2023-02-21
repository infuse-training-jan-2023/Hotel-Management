from service.booking_service import BookingService
from flask import Response,request
from bson import json_util
import json
class BookingController:
    def book_room(self):
        try:
            request_data = request.get_json()
            booking_data=BookingService.book_room(request_data)
            return Response(json.dumps(booking_data), mimetype='application/json', status=201)
        except Exception as e:
            return str(e)
  
    def cancel_booking(self):
        try:
            booking_id = request.get_json()
            booking_data=BookingService.cancel_booking(booking_id)
            return Response(json.dumps(booking_data), mimetype='application/json', status=200)
        except Exception as e:
            return str(e)   
    
    def get_user_booking_by_email(self):
        try:
            customer_email = request.args.get('customer_email')
            booking_data=BookingService.get_user_booking_by_email(customer_email)
            return Response(json_util.dumps(booking_data), mimetype='application/json', status=200)
        except Exception as e:
            return str(e)
    
    def calculate_discount(self):
        try:
            customer_email = request.args.get('customer_email')
            discount = BookingService.calculate_discount(customer_email)
            return Response(json.dumps({"discount":discount}), status=200, mimetype="application/json")
        except Exception as e:
            return str(e)