from flask import Blueprint,Response,request
import sys
sys.path.insert(0, './controller')
from invoice import InvoiceController

pdf_bp=Blueprint('pdf_bp',__name__)

@pdf_bp.route("/pdf", methods=['GET'])
def invoice():
    bill = InvoiceController()
    id = request.args.get('id')
    pdf = bill.get_invoice(id)
    return Response(pdf,status=200, mimetype='application/pdf')
    
