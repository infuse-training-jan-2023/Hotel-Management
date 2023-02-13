import sys
sys.path.insert(0, './service')
from customer_service import CustomerService
class CustomerController:
    def get_customer_details(email):
      try:
        customer=CustomerService.get_customer(email)
        resp = {
          '_id': customer["_id"],
          'name': customer["name"],
          'email': customer["email"],
          'phone_number': customer["phone_number"],
          'address': customer["address"]
        
           }
        # print(resp)
        return resp
      except Exception as e:
        return str(e) 
