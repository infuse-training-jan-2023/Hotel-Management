from connect import Connection
from Model.review_schema import review_validator
from Model.add_ons_schema import addons_validator
from Model.booking_schema import booking_validator
from Model.rooms_schema import rooms_validator

Connection.db.create_collection('review', validator=review_validator)
Connection.db.create_collection('room', validator=rooms_validator)
Connection.db.create_collection('booking', validator=booking_validator)
Connection.db.create_collection('add_ons', validator=addons_validator)
