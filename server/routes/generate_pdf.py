from flask import Blueprint,Response
import sys
sys.path.insert(0, './controller')
from invoice import InvoiceController

pdf_bp=Blueprint('pdf_bp',__name__)

@pdf_bp.route("/api/pdf", methods=['GET'])
def invoice():
    bill = InvoiceController()
    id = '63e8990dd86932d6faf1e4d1'
    pdf = bill.get_invoice(id)
    return Response(pdf,status=200, mimetype='application/pdf')
    
