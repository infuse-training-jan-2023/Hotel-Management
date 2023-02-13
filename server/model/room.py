    
from pymongo import MongoClient# define the schema

room_schema = {
  "room_no": int,
  "room_type": str,
  "price": float,
  "capacity": int,
  "amenities": list,
  "images": list
}

# create a model from the schema
# client = MongoClient('mongodb://localhost:27017')
# db = client['my_database']
# users = db.users