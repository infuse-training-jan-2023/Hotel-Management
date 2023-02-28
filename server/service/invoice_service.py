from DB.connect import Connection
from bson.objectid import ObjectId
import pymongo
from datetime import datetime
from fpdf import FPDF

class Invoice:
    @staticmethod
    def generate_invoice(id):
        try:
            cb = Connection.db.booking.find_one({"_id": ObjectId(id)})
            room = Connection.db.room.find_one({"_id": ObjectId(cb["room_id"])})
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial","B", size = 20)
            pdf.cell(200, 10,"The New View",ln = 1,align='C')
            pdf.set_font("Arial","B", size=15)
            pdf.cell(0, 20, "Booking Details",ln = 1, align='L')
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 8, f"BID: {cb.get('_id')}",ln=1, align='L')
            pdf.cell(0, 8, f"Customer Name: {cb.get('guest_name')}", ln=1,align='L')
            pdf.cell(0, 8, f"Email: {cb.get('customer_email')}", ln=1, align='L')
            pdf.cell(0, 8, f"Phone No: {cb.get('phone_number')}", ln=1,align='L')
            pdf.cell(0, 8, f"Check In: {datetime.date(cb.get('check_in'))}", ln=1, align='L')
            pdf.cell(0, 8, f"Check Out: {datetime.date(cb.get('check_out'))}", ln=1,align='L')
            pdf.cell(0, 8, f"Room Name: {room.get('title')}", ln=1, align='L')
            pdf.cell(0, 8, f"Room Type: {room.get('room_type')}", ln=1, align='L')
            pdf.cell(0, 8, f"Amenities: {', '.join([str(amenitie) for amenitie in room.get('amenities')])}", ln=1,align='L')
            pdf.cell(0, 8, f"Special Request: {cb.get('special_request')}", ln=1, align='L')
            pdf.set_font("Arial","B", size=15)
            pdf.cell(0, 20, "Payment Info",ln = 1, align='L')
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 8, f"Room Price: + Rs {cb.get('room_price')}", ln=1, align='L')
            add_ons_str = ', '.join([str(add_on) for add_on in cb.get('add_ons')])
            data = add_ons_str.translate(str.maketrans("", "", "{'},]")).split()
            data =  data[1::2]     
            for i in range(0, len(data), 2):
                pdf.cell(0, 8, f"{data[i]}: + Rs {data[i+1]}",ln=1,align='L') 
            pdf.cell(0, 8, f"Discount: - Rs {cb.get('discount')}", ln=1, align='L')
            pdf.set_font("Arial","B", size=15)
            pdf.cell(0, 15, f"Total Amount: Rs {cb.get('total_amount')}/-", ln=1, align='L') 
            return pdf
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
