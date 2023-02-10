from flask import Blueprint,Flask, Response, request
import json
from controller.add_on_controller import AddonController

add_on_bp=Blueprint('add_on_bp',__name__)
@add_on_bp.route('/api/add-ons',methods=['GET'])
def get_add_ons():
    add_on_controller=AddonController()
    add_on_data=add_on_controller.get_all_add_ons()
    return Response(json.dumps(add_on_data), mimetype='application/json', status=200)