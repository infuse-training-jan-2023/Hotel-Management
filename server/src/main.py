from flask import Flask ,request , Response
import json
from bson import json_util
from pymongo import MongoClient 
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('mongodb+srv://mongodb:mongodb@cluster0.uxi24a7.mongodb.net/?retryWrites=true&w=majority')
db = client['hotel']
collection = db.customer
room = db.room
booking_collection = db.booking

app = Flask(__name__)

@app.route("/api/booking", methods = ['POST'])
def book_room():
    request_data = request.get_json()
    print(request_data)
    data = {"FK_id": ObjectId("5126bc054aed4daf9e2ab772"), "name": "user"}
    booking_collection.insert_one(data).inserted_id
    return Response(json.dumps({'id':'{id}' , 'name':'hello' }), mimetype='application/json', status=200)

@app.route("/api/booking", methods = ['GET'])
def booking_details():
    bookings_list =[]
    for booking_details in booking_collection.find():
        bookings_list.append(booking_details)
        print(booking_details["_id"])

    print(booking_collection.find_one({"FK_id": ObjectId("5126bc054aed4daf9e2ab772")}))
    return Response(json_util.dumps(bookings_list), mimetype='application/json', status=200)
    #return json.loads(json_util.dumps(bookings_list))
   

@app.route("/api/cancel")
def cancel_booking():
    return Response(json.dumps(room.find()),mimetype='application/json', status=200)

if __name__ == "__main__":
    app.run(debug=True)