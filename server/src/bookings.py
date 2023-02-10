import datetime
from datetime import date
import sys
sys.path.insert(0, './DB')
from room import Room

class Bookings:

    def __init__(self , request_data) -> None:
         self.booking_data = request_data

    def create_booking_record(self):
      
        room = Room()

        id = self.booking_data.get("room_id")
        room_price =room.get_room_price(id)
        room_cost = room_price*self.get_no_of_days()
        add_ons_cost = self.get_add_ons_cost(self.booking_data.get("add_ons"))
        print("total cost", add_ons_cost+room_cost)
        total_amount= add_ons_cost+room_cost
        return self.format_booking_record(total_amount , room_price)

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

    def format_booking_record(self, total_amount, room_price):
        check_in = self.booking_data.get("check_in")
        check_out = self.booking_data.get("check_out")
        add_on = self.booking_data.get("add_ons")
        customer_id = self.booking_data.get("customer_id")
        room_id = self.booking_data.get("room_id")
        cancel_status = False

        return {"check_in":check_in, "check_out":check_out, "add_ons":add_on ,"total_amount":total_amount, "room_price":room_price, "customer_id":customer_id, "room_id":room_id, "cancel_status":cancel_status }
        



# request_data ={
#                "check_in":datetime.datetime(2023, 2, 10),
#                "check_out":datetime.datetime(2023, 2, 16),
#                "room_id":"63e523f1964c58b41d4dc86f",
#                "customer_id":"63e52044ba29b6d46527fe93",
#                "add_ons":[{"service":"gym", "price":500},{"service":"break fast", "price":700}]
#                }
# obj =Bookings(request_data)
# record = obj.create_booking_record()
# print(record)



