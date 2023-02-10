from flask import Flask, request, Response
import json
from datetime import datetime

import sys
sys.path.insert(0, './DB')
from customer import  Customer
from booking import Booking
from bson import json_util

from room import Room



app = Flask(__name__)


@app.route('/api/room/<int:room_no>',methods=['GET'])
def get_room(room_no):
    room= Room()
    room_resp=room.get_room_details(room_no)
    res = {
          'room_no': room_resp["room_no"],
          'room_type': room_resp["room_type"],
          'price': room_resp["price"],
          'capacity': room_resp["capacity"],
          'amenities': room_resp["amenities"],
          'images' : room_resp["images"]
           }
     
    print(res)
    return Response(json.dumps(res), mimetype='application/json', status=200)

@app.route('/api/add-ons',methods=['GET'])
def get_add_ons():
    add_on_data=add_on_actions.get_all_add_ons()
    return Response(json.dumps(add_on_data), mimetype='application/json', status=200)










@app.route("/api/search", methods = ['GET'])
def get_all_rooms():
    customer = Customer()
    rooms = customer.get_all_rooms()
    return Response(json_util.dumps(rooms), status=200, mimetype="application/json")

@app.route("/api/loyalty-discount", methods = ['GET'])
def add_one_room():
    booking = Booking()
    id = request.args.get('id')
    count = booking.calculate_discount(id)
    return Response(json.dumps({"discount":count*10}), status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)