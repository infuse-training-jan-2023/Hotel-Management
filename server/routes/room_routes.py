from flask import Blueprint

from controller.room_controller import RoomController

room_bp = Blueprint('room_bp', __name__)

@room_bp.route('/room',methods=['GET'])
def get_room_details():
    return RoomController().get_room_details()
    
@room_bp.route("/rooms", methods = ['GET'])
def get_all_rooms():
    return RoomController().get_all_rooms()
    
@room_bp.route("/available/rooms", methods = ['POST'])
def get_available_rooms():
    return RoomController().get_available_rooms()
    