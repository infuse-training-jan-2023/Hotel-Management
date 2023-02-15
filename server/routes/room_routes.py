from flask import Blueprint

from controller.room_controller import RoomController

room_bp = Blueprint('room_bp', __name__)

@room_bp.route('/rooms',methods=['GET'])
def get_room():
    return RoomController().get_room_details()
    
@room_bp.route("/search", methods = ['POST'])
def get_all_rooms():
    return RoomController().get_all_rooms()
    