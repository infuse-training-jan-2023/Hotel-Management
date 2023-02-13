from flask import Flask
from routes.customer_review import review_bp
from routes.customer_booking import booking_bp
from routes.search import search_bp
from routes.generate_pdf import pdf_bp
from routes.room_routes import room_bp
from routes.add_on_routes import add_on_bp
from routes.bookings_routes import bookings_bp

app = Flask(__name__)

app.register_blueprint(review_bp)
app.register_blueprint(booking_bp)	
app.register_blueprint(search_bp)
app.register_blueprint(pdf_bp)
app.register_blueprint(room_bp)
app.register_blueprint(add_on_bp)
app.register_blueprint(bookings_bp)


if __name__ == "__main__":
    app.run(debug=True)





