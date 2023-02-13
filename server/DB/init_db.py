from connect import Connection
import sys
sys.path.insert(0, './Model')
from review_schema import review_validator
from customer_schema import customer_validator
from add_ons_schema import addons_validator
from booking_schema import booking_validator
from rooms_schema import rooms_validator

Connection.db.create_collection('review', validator=review_validator)
Connection.db.create_collection('customer', validator=customer_validator)
Connection.db.create_collection('room', validator=rooms_validator)
Connection.db.create_collection('booking', validator=booking_validator)
Connection.db.create_collection('add_ons', validator=addons_validator)
