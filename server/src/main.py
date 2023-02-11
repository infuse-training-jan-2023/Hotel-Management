import sys
sys.path.insert(0, './routes')
from flask import Flask
from customer_review import review_bp
from customer_booking import booking_bp
from search import search_bp

app = Flask(__name__)

app.register_blueprint(review_bp)
app.register_blueprint(booking_bp)	
app.register_blueprint(search_bp)


if __name__ == "__main__":
    app.run(debug=True)