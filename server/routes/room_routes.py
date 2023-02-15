from flask import Blueprint, Response
from bson import json_util
from controller.room_controller import RoomController

room_bp = Blueprint('room_bp', __name__)

@room_bp.route('/rooms',methods=['GET'])
def get_room():
    room_data=RoomController().get_room_details()
    return Response(json_util.dumps(room_data), mimetype='application/json', status=200)

@room_bp.route("/search", methods = ['POST'])
def get_all_rooms():
    rooms = RoomController().get_all_rooms()
    return Response(json_util.dumps(rooms), status=201, mimetype="application/json")