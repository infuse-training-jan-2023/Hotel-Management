from flask import Flask, request, Response, jsonify
from flask_mongoengine import MongoEngine

from routes.bookings_routes import booking_bp


app = Flask(__name__)

app.register_blueprint(booking_bp)


if __name__ == "__main__":
    app.run(debug=True)