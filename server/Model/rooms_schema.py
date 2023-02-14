rooms_validator = {
    "$jsonSchema": {
    "bsonType": "object",
    "required": ["room_no", "room_type","price","capacity","amenities","images","description"],
    "properties":{
        "room_no": {
            "bsonType": "number",
            },
        "room_type": {
            "bsonType": "string",
            },
        "price": {
            "bsonType": "number",
            },
        "capacity": {
            "bsonType": "number",
            },
        "amenities": {
            "bsonType": "array",
            },
        "images": {
            "bsonType": "array"
            },
        "description": {
            "bsonType": "string"
            } 
        }
    }         
}
