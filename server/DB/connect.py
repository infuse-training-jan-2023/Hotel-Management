from pymongo import MongoClient

class Connection:
    cluster = MongoClient('mongodb+srv://mongodb:mongodb@cluster0.uxi24a7.mongodb.net/?retryWrites=true&w=majority')
    db = cluster['hotel2']
    customer = db.customers
    room = db.rooms
    booking = db.bookings
