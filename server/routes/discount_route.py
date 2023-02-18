from flask import Blueprint 
from controller.discount_controller import DiscountController

discount_bp = Blueprint('discount_bp', __name__)

    
@discount_bp.route("/loyalty-discount", methods = ['GET'])
def calc_discount():
   return DiscountController().calculate_discount()
    