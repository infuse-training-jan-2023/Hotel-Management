import datetime
from datetime import date

class Bookings:

    def __init__(self , request_data) -> None:
         self.booking_data = request_data

    def create_booking_record(self):
        room_price= 1000
       
        print(room_price*self.get_no_of_days(), "amount")
        print(self.get_add_ons_cost(self.booking_data.get("add_ons")))



        
    
    def get_no_of_days(self):
        chk_in_date = self.booking_data.get("check_in")
        chk_out_date = self.booking_data.get("check_out")
        delta_days = chk_out_date - chk_in_date
        return delta_days.days
    
    def get_add_ons_cost(self , add_ons):
        addons_cost=0
        for service in add_ons:
             addons_cost += service.get("price")
        return addons_cost

    def get_room_price(self):
        print()




request_data ={"name":"user1" ,
               "contacts":"1234567892" , 
               "email":"users@gmail.com" ,
               "check_in":date(2023, 2, 10),
               "check_out":date(2023, 2, 16),
               "room_id":"63e523f1964c58b41d4dc86f",
               "add_ons":[{"service":"gym", "price":500},{"service":"break fast", "price":700}]
               }

obj =Bookings(request_data)
obj.create_booking_record()

