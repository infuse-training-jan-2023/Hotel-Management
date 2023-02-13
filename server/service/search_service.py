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
                #print(f'from {from_date} to {to_date}')
                date_filters ={'$or': [
                { 'check_in': { '$gte': from_date, '$lte': to_date } },
                { 'check_out': { '$gte': from_date, '$lte': to_date }},
                { '$and': [
                    { 'check_in': { '$lte': from_date } }, 
                    { 'check_out': { '$gte': to_date } }
                    ]
                },
                ]}
                del filters["check_in"], filters['check_out']
                unavailable = Connection.booking.find(date_filters)
                unavailable_ids = [x.get('room_id') for x in unavailable]
                # for x in unavailable_ids:
                #     print(x)
                filters['_id'] =  { '$nin': unavailable_ids }
                available = Connection.room.find(filters)

            print(filters)
            available = Connection.room.find(filters)
            return available
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
