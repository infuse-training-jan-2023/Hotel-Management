from service.invoice_service import Invoice
from flask import request, make_response
class InvoiceController:
    def generate_invoice(self):
        try:
            id = request.args.get('id')
            pdf = Invoice.generate_invoice(id)
            response = make_response(pdf.output(dest='S').encode('latin-1'))
            response.headers.set('Content-Disposition', 'attachment')
            response.headers.set('Content-Type', 'application/pdf')
            return response
        except Exception as e:
            return str(e)