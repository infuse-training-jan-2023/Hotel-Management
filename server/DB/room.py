import json
from bson import json_util
from booking import Booking

from connect import Connection

class Room:
    def get_all_rooms(self, filters):
        
        if filters.keys() >= {'checkin', 'checkout'}:
            from_date = filters.get('checkin')
            to_date = filters.get('checkout')
            date_filters ={'$or': [
              { 'start': { '$gte': from_date, '$lte': to_date } },
              { 'end': { '$gte': from_date, '$lte': to_date }},
              { '$and': [
                { 'start': { '$lte': from_date } }, 
                { 'end': { '$gte': to_date } }
                ]
              },
            ]}
            del filters["checkin"], filters['checkout']
            unavailable = Connection.booking.find(date_filters)
            unavailable_ids = [x.get('room') for x in unavailable]
            filters['_id'] =  { '$nin': unavailable_ids }
            available = Connection.room.find(filters)

        print(filters)
        available = Connection.room.find(filters)
        return available

    
