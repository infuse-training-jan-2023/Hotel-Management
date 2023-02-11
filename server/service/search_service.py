import sys
import pymongo
sys.path.insert(0, './DB')
from connect import Connection

class Room:
    @staticmethod
    def get_all_rooms(filters):
        try:
            if filters.keys() >= {'check_in', 'check_out'}:
                from_date = filters.get('check_in')
                to_date = filters.get('check_out')
                date_filters ={'$or': [
                { 'start': { '$gte': from_date, '$lte': to_date } },
                { 'end': { '$gte': from_date, '$lte': to_date }},
                { '$and': [
                    { 'start': { '$lte': from_date } }, 
                    { 'end': { '$gte': to_date } }
                    ]
                },
                ]}
                del filters["check_in"], filters['check_out']
                unavailable = Connection.booking.find(date_filters)
                unavailable_ids = [x.get('room') for x in unavailable]
                filters['_id'] =  { '$nin': unavailable_ids }
                available = Connection.room.find(filters)

            print(filters)
            available = Connection.room.find(filters)
            return available
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
