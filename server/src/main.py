from flask import Flask, request, Response
import json
from datetime import datetime
from pprint import pprint

import sys
sys.path.insert(0, './DB')
from room import  Room
from booking import Booking
from bson import json_util

app = Flask(__name__)

@app.route("/api/search", methods = ['POST'])
def get_all_rooms():
    room = Room()
    #{"checkin":"2023-02-21","checkout":"2023-02-07","room_type":"double","price":0}
    request_data = request.get_json()
    checkin = request_data.get('checkin')
    checkout = request_data.get('checkout')
    room_type = request_data.get('room_type')
    price = request_data.get('price')
    if price:
        price = {"$gt":int(price)}
    
    if checkin and checkout:
        checkin = datetime.strptime(checkin, '%Y-%m-%d')
        checkout = datetime.strptime(checkout, '%Y-%m-%d')
    else:
        checkin=checkout=None

    #print(f'checkin: {type(checkin)} checkout: {type(checkout)} room_type: {type(room_type)} price: {type(price)}')
    data = {'checkin':checkin, 'checkout':checkout, 'type':room_type, 'price':price}
    filtered = {k: v for k, v in data.items() if v is not None}
    data.clear()
    data.update(filtered)
    
    rooms = room.get_all_rooms(data)
    return Response(json_util.dumps(rooms), status=200, mimetype="application/json")

@app.route("/api/room/<string:id>", methods = ['GET'])
def get_one_room(id):
    room = Room()
    room_doc = room.get_one_room(id)
    return Response(json_util.dumps(room_doc), status=200, mimetype="application/json")



@app.route("/api/loyalty-discount", methods = ['GET'])
def calc_discount():
    booking = Booking()
    id = request.args.get('id')
    discount = booking.calculate_discount(id)
    return Response(json.dumps({"discount":discount}), status=200, mimetype="application/json")



if __name__ == "__main__":
    app.run(debug=True)