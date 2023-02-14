from flask import Blueprint, Response,request
from datetime import datetime
import sys
sys.path.insert(0, './controller')
from bson import json_util
from search_room import SearchController

search_bp=Blueprint('search_bp',__name__)
@search_bp.route("/search", methods = ['POST'])
def get_all_rooms():
    room = SearchController()
    #{"checkin":"2023-02-21","checkout":"2023-02-07","room_type":"double","price":0}
    request_data = request.get_json()
    check_in = request_data.get('check_in')
    check_out = request_data.get('check_out')
    room_type = request_data.get('room_type')
    price = request_data.get('price')
    if price:
        price = {"$gt":int(price)}
    
    if check_in and check_out:
        check_in = datetime.strptime(check_in, '%Y-%m-%d')
        check_out = datetime.strptime(check_out, '%Y-%m-%d')
    else:
        check_in=check_out=None

    #print(f'checkin: {type(checkin)} checkout: {type(checkout)} room_type: {type(room_type)} price: {type(price)}')
    data = {'check_in':check_in, 'check_out':check_out, 'room_type':room_type, 'price':price}
    filtered = {k: v for k, v in data.items() if v is not None}
    data.clear()
    data.update(filtered)
    
    rooms = room.get_all_rooms(data)
    return Response(json_util.dumps(rooms), status=201, mimetype="application/json")