from service.invoice_service import Invoice
from flask import request
class InvoiceController:
    def generate_invoice(self):
        try:
            id = request.args.get('id')
            pdf = Invoice.generate_invoice(id)
            return pdf
        except Exception as e:
            return str(e)