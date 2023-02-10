from flask import Flask, request, Response
import json
from datetime import datetime

import sys
sys.path.insert(0, './DB')
from customer import  Customer
from booking import Booking
from bson import json_util

app = Flask(__name__)

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