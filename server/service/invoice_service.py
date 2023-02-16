from DB.connect import Connection
from bson.objectid import ObjectId
import pymongo
from io import BytesIO
from datetime import datetime
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
            c.drawString(100, 750, "Booking Details")
            c.setFont("Helvetica", 12)
            c.drawString(100, 700 , f"Customer Name: {cb.get('guest_name')}")
            c.drawString(100, 675 , f"Email: {cb.get('customer_email')}")
            c.drawString(100, 650 , f"Phone No: {cb.get('phone_number')}")
            c.drawString(100, 625 , f"Check In: {datetime.date(cb.get('check_in'))}")
            c.drawString(100, 600 , f"Check Out: {datetime.date(cb.get('check_out'))}")
            c.drawString(100, 575 , f"Room Type: {room.get('room_type')}")
            c.drawString(100, 550 , f"Room No: {room.get('room_no')}")
            c.drawString(100, 525 , f"Amenities: {', '.join([str(amenitie) for amenitie in room.get('amenities')])}")
            c.drawString(100, 500 , f"Special Request: {cb.get('special_request')}")
            c.drawString(100, 475 , f"Room Price: {cb.get('room_price')}")
            add_ons_str = ', '.join([str(add_on) for add_on in cb.get('add_ons')])
            data = add_ons_str.replace('{','').replace('}','').replace("'","")
            c.drawString(100, 450 , f"Add-Ons: {data}")
            c.drawString(100, 425 , f"Discount: {cb.get('discount')}") 
            c.drawString(100, 400 , f"Total Amount: {cb.get('total_amount')}")          
            c.save()
            pdf = buffer.getvalue()
            return pdf
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
