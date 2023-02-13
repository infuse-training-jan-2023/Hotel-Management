from flask import Blueprint, Response, request
from bson import json_util
import sys
sys.path.insert(0, './controller')
from room_controller import RoomController
room_bp = Blueprint('room_bp', __name__)

@room_bp.route('/api/room',methods=['GET'])
def get_room():
    room_id = request.args.get('room_id')
    room_controller=RoomController()
    room_data=room_controller.get_room_details(room_id)
    print(room_data)
    return Response(json_util.dumps(room_data), mimetype='application/json', status=200)



