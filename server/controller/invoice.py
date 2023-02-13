import sys
sys.path.insert(0, './service')
from invoice_service import Invoice

class InvoiceController:
    def get_invoice(self,id):
        try:
            pdf = Invoice.get_invoice(id)
            return pdf
        except Exception as e:
            return str(e)