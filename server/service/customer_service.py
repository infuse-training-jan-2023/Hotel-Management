from DB.connect import Connection
import pymongo

class CustomerService:
    @staticmethod
    def get_customer(email):
        try:
            customer_data = Connection.db.customer.find_one({"email": email})
            return customer_data
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
    
   