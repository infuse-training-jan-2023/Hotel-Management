from flask import Blueprint, Response
from bson import json_util
from controller.search_room import SearchController

search_bp=Blueprint('search_bp',__name__)
@search_bp.route("/api/search", methods = ['POST'])
def get_all_rooms():
    rooms = SearchController().get_all_rooms()
    return Response(json_util.dumps(rooms), status=201, mimetype="application/json")