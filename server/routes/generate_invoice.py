from flask import Blueprint,Response
from controller.generate_invoice_controller import InvoiceController

pdf_bp=Blueprint('pdf_bp',__name__)

@pdf_bp.route("/api/invoice", methods=['GET'])
def invoice():
    pdf = InvoiceController().generate_invoice()
    return Response(pdf,status=200, mimetype='application/pdf')
    
