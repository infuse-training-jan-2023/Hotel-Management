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
            c.setFont("Helvetica-Bold", 20)
            c.drawString(230, 760, "The New View")
            c.setFont("Helvetica-Bold", 15)
            c.drawString(100, 725, "Booking Details")
            c.setFont("Helvetica", 12)
            c.drawString(100, 700 , f"BID: {cb.get('_id')}")
            c.drawString(100, 675 , f"Customer Name: {cb.get('guest_name')}")
            c.drawString(100, 650 , f"Email: {cb.get('customer_email')}")
            c.drawString(100, 625 , f"Phone No: {cb.get('phone_number')}")
            c.drawString(100, 600 , f"Check In: {datetime.date(cb.get('check_in'))}")
            c.drawString(100, 575 , f"Check Out: {datetime.date(cb.get('check_out'))}")
            c.drawString(100, 550 , f"Room Type: {room.get('room_type')}")
            c.drawString(100, 525 , f"Amenities: {', '.join([str(amenitie) for amenitie in room.get('amenities')])}")
            c.drawString(100, 500 , f"Special Request: {cb.get('special_request')}")
            c.setFont("Helvetica-Bold", 15)
            c.drawString(100, 450, "Payment Info")
            c.setFont("Helvetica", 12)
            c.drawString(100, 425 , f"Room Price: + Rs {cb.get('room_price')}")
            add_ons_str = ', '.join([str(add_on) for add_on in cb.get('add_ons')])
            data = add_ons_str.replace('{','').replace('}','').replace("'","").replace(",","").split(" ")
            c.drawString(100, 400 , f'{data[1] +": + Rs "+data[3]}')
            c.drawString(100, 375 , f'{data[5] +": + Rs "+data[7]}')
            c.drawString(100, 350 , f"Discount: - Rs {cb.get('discount')}") 
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, 320 , f"Total Amount: Rs {cb.get('total_amount')}")          
            c.save()
            pdf = buffer.getvalue()
            return pdf
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
