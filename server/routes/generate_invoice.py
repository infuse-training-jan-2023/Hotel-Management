from flask import Blueprint,Response
from controller.generate_invoice_controller import InvoiceController

pdf_bp=Blueprint('pdf_bp',__name__)

@pdf_bp.route("/invoice", methods=['GET'])
def invoice():
    return InvoiceController().generate_invoice()
    
    
