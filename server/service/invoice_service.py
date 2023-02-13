import sys
sys.path.insert(0, './DB')
from connect import Connection
from bson.objectid import ObjectId
import pymongo
from io import BytesIO
from reportlab.pdfgen import canvas

class Invoice:
    @staticmethod
    def get_invoice(id):
        try:
            cb = Connection.booking.find_one({"_id": ObjectId(id)})
            customer = Connection.customer.find_one({"_id": ObjectId(cb["customer_id"])})
            room = Connection.room.find_one({"_id": ObjectId(cb["room_id"])})
            buffer = BytesIO()
            c = canvas.Canvas(buffer)
            c.setFont("Helvetica-Bold", 15)
            c.drawString(100, 750, "Customer Details")
            c.setFont("Helvetica", 11)
            c.drawString(100, 725 , f"Name: {customer.get('name')}")
            c.drawString(100, 700 , f"Email: {customer.get('email')}")
            c.drawString(100, 675 , f"Phone No: {customer.get('phone_number')}")
            c.drawString(100, 650 , f"Address: {customer.get('address')}")
            c.drawString(100, 625 , f"Room Type: {room.get('room_type')}")
            c.drawString(100, 600 , f"Room No: {room.get('room_no')}")
            c.drawString(100, 575 , f"Check In: {cb.get('check_in')}")
            c.drawString(100, 550 , f"Check Out: {cb.get('check_out')}")
            c.drawString(100, 525 , f"Add-Ons: {', '.join([str(add_on) for add_on in cb.get('add_ons')])}")
            c.drawString(100, 500 , f"Room Price: {cb.get('room_price')}")
            c.drawString(100, 475 , f"Total Amount: {cb.get('total_amount')}")
            c.setFont("Helvetica-Bold", 15)
            c.drawString(100,425, "Guest Details")
            c.setFont("Helvetica", 11)
            c.drawString(100, 400 , f"Guest Name: {cb.get('guest_name')}")
            c.drawString(100, 375 , f"Email: {cb.get('email')}")
            c.drawString(100, 350 , f"Phone No: {cb.get('phone_number')}")
            c.drawString(100, 325 , f"Special Request: {cb.get('special_request')}")
            c.save()
            pdf = buffer.getvalue()
            return pdf
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
