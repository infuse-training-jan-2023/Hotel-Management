from flask import Blueprint, Response, request
import json
import sys
sys.path.insert(0, './controller')
from add_on_controller import AddonController

add_on_bp=Blueprint('add_on_bp',__name__)
@add_on_bp.route('/api/add_ons',methods=['GET'])
def get_add_ons():
    add_on_controller=AddonController()
    add_on_data=add_on_controller.get_all_add_ons()
    return Response(json.dumps(add_on_data), mimetype='application/json', status=200)