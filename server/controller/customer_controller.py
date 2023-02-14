from service.customer_service import CustomerService
from flask import  request

class CustomerController:
    def get_customer_details():
      try:
        email = request.args.get('email')
        customer=CustomerService.get_customer(email)
        resp = {
          '_id': customer["_id"],
          'name': customer["name"],
          'email': customer["email"],
          'phone_number': customer["phone_number"],
          'address': customer["address"]
        
           }
        return resp
      except Exception as e:
        return str(e) 
