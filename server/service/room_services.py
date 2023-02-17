from DB.connect import Connection
import pymongo
from bson.objectid import ObjectId
from datetime import datetime

class RoomService:
    @staticmethod
    def get_room(room_id):
        try:
            result = Connection.db.room.find_one({"_id": ObjectId(room_id)})
            return result
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
    
    @staticmethod
    def get_all_rooms():
        try:
            rooms = Connection.db.room.find()
            return rooms
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
            

    @staticmethod
    def get_available_rooms(filters):
        check_in = filters.get('check_in')
        check_out = filters.get('check_out')
        room_type = filters.get('room_type')
        price = filters.get('price')
        try:
            if price:
                price = {"$gt":int(price)}
            if check_in and check_out:
                check_in = datetime.strptime(check_in, '%Y-%m-%d')
                check_out = datetime.strptime(check_out, '%Y-%m-%d')
            else:
                check_in=check_out=None
            if room_type=='any':
                room_type=None
                
            print(f'checkin: {check_in} checkout: {check_out} room_type: {room_type} price: {price}')
            data = {'check_in':check_in, 'check_out':check_out, 'room_type':room_type, 'price':price}
            filtered = {k: v for k, v in data.items() if v is not None}
            data.clear()
            data.update(filtered)            

            if data.keys() >= {'check_in', 'check_out'}:
                from_date = data.get('check_in')
                to_date = data.get('check_out')
                date_filters ={'$or': [
                { 'check_in': { '$gte': from_date, '$lte': to_date } },
                { 'check_out': { '$gte': from_date, '$lte': to_date }},
                { '$and': [
                    { 'check_in': { '$lte': from_date } }, 
                    { 'check_out': { '$gte': to_date } }
                    ]
                },
                ]}
                del data["check_in"], data['check_out']
                unavailable = Connection.db.booking.find(date_filters)
                unavailable_ids = [x.get('room_id') for x in unavailable]
                data['_id'] =  { '$nin': unavailable_ids }
                available = Connection.db.room.find(data)
            available = Connection.db.room.find(data)
            return available
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)

            
