from DB.connect import Connection
from bson.objectid import ObjectId
import pymongo
from io import BytesIO
from reportlab.pdfgen import canvas

class Invoice:
    @staticmethod
    def generate_invoice(id):
        try:
            cb = Connection.db.booking.find_one({"_id": ObjectId(id)})
            room = Connection.db.room.find_one({"_id": ObjectId(cb["room_id"])})
            buffer = BytesIO()
            c = canvas.Canvas(buffer)
            c.setFont("Helvetica-Bold", 15)
            c.drawString(100, 750, "Customer Details")
            c.setFont("Helvetica", 11)
            c.drawString(100, 700 , f"Customer Name: {cb.get('guest_name')}")
            c.drawString(100, 675 , f"Email: {cb.get('customer_email')}")
            c.drawString(100, 650 , f"Phone No: {cb.get('phone_number')}")
            c.drawString(100, 625 , f"Check In: {cb.get('check_in')}")
            c.drawString(100, 600 , f"Check Out: {cb.get('check_out')}")
            c.drawString(100, 575 , f"Room Type: {room.get('room_type')}")
            c.drawString(100, 550 , f"Room No: {room.get('room_no')}")
            c.drawString(100, 525 , f"Add-Ons: {', '.join([str(add_on) for add_on in cb.get('add_ons')])}")
            c.drawString(100, 500, f"Special Request: {cb.get('special_request')}")
            c.drawString(100, 475 , f"Room Price: {cb.get('room_price')}")
            c.drawString(100, 450 , f"Total Amount: {cb.get('total_amount')}")          
            c.save()
            pdf = buffer.getvalue()
            return pdf
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
