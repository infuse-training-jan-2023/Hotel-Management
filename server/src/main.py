from flask import Flask, request, Response, jsonify
from flask_mongoengine import MongoEngine
import json
from datetime import datetime
from bookings import Bookings


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

@app.route("/api/book", methods = ['POST'])
def book_room():
    request_data ={
               "check_in":datetime(2023, 2, 25),
               "check_out":datetime(2023, 2, 26),
               "room_id":"63e523f1964c58b41d4dc869",
               "customer_id":"63e52044ba29b6d46527fe93",
               "add_ons":[{"service":"gym", "price":500},{"service":"break fast", "price":700}]
               }
    obj =Bookings(request_data)
    record = obj.create_booking_record()
    booking = Booking()
    booking.add_booking(record)
    return Response(json_util.dumps({"added":record}), status=201, mimetype="application/json")

@app.route("/api/book", methods = ['DELETE'])
def cancel_booking():
    request_data ={
               "booking_id":"63e60625b1faae5832b986e7",
               }

    booking = Booking()
    booking.cancel_booking(request_data.get("booking_id"))
    return Response(json_util.dumps({"msg":"booking canceled"}), status=200, mimetype="application/json")


@app.route("/api/book", methods = ['GET'])
def get_booking():

    request_data ={
               "check_in":datetime(2023, 2, 10),
               "check_out":datetime(2023, 2, 16),
               "room_id":"63e523f1964c58b41d4dc86f",
               "customer_id":"63e52044ba29b6d46527fe93",
               "add_ons":[{"service":"gym", "price":500},{"service":"break fast", "price":700}]
               }
    obj =Bookings(request_data)
    record = obj.create_booking_record()
    val=MyBooking(**record).save
    print(jsonify(val))
    movies = MyBooking.objects()
    print(movies)
    return  jsonify(movies), 200

app.config['MONG_DBNAME'] = 'hotel'
app.config["MONGODB_HOST"] = "mongodb+srv://mongodb:mongodb@cluster0.uxi24a7.mongodb.net/?retryWrites=true&w=majority"
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'hotel',
#     'host': 'mongodb+srv://mongodb:mongodb@cluster0.uxi24a7.mongodb.net/?retryWrites=true&w=majority',
#     'port': 27017
# }
db = MongoEngine()
db.init_app(app)


class MyCustomer(db.Document):
    name = db.StringField()

class MyRoom(db.Document):
    room = db.StringField()

class MyBooking(db.Document):
    check_in = db.DateField()
    check_out = db.DateField()
    add_ons = db.ListField()
    total_amount = db.FloatField()
    room_price = db.FloatField()
    customer_id = db.ReferenceField(MyCustomer)
    room_id = db.ReferenceField(MyRoom)
    cancel_status = db.BooleanField()

if __name__ == "__main__":
    app.run(debug=True)