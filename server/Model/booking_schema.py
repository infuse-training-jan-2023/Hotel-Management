booking_validator = {
    "$jsonSchema": {
    "bsonType": "object",
    "required": ["check_in","check_out","add_ons","total_amount","room_price","customer_email","room_id","isCancelled","guest_name","phone_number","special_request","discount"],
    "properties":{
        "check_in": {
            "bsonType": "date",
            },
        "check_out": {
            "bsonType": "date",
            },
        "add_ons": {
            "bsonType": "array",
            },
        "total_amount": {
            "bsonType": "number",
            },
        "room_price": {
            "bsonType": "number",
            },
        "customer_email": {
            "bsonType": "string",
            },
        "room_id": {
            "bsonType": "objectId",
            },
        "isCancelled": {
            "bsonType": "bool",
            },
        "guest_name": {
            "bsonType": "string",
            },
        "phone_number": {
            "bsonType": "string",
            },
        "special_request": {
            "bsonType": "string"
            },
        "discount": {
            "bsonType": "number"
            }
        }
    }         
}
