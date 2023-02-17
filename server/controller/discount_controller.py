from service.discount_service import DiscountService
from flask import Response,request
from bson import json_util
import json
class DiscountController:
   
    def calculate_discount(self):
        try:
            customer_email = request.args.get('customer_email')
            discount = DiscountService.calculate_discount(customer_email)
            return Response(json.dumps({"discount":discount}), status=200, mimetype="application/json")
        except Exception as e:
            return str(e)