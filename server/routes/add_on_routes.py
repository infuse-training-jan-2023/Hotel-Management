from flask import Blueprint
from controller.add_on_controller import AddonController

add_on_bp=Blueprint('add_on_bp',__name__)

@add_on_bp.route('/addons',methods=['GET'])
def get_add_ons():
    add_on_controller=AddonController()
    return add_on_controller.get_all_add_ons()