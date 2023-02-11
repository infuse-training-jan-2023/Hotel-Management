booking_validator = {
    "$jsonSchema": {
    "bsonType": "object",
    "required": ["check_in","check_out","add_ons","total_amount","room_price","customer_id","room_id","cancel_status"],
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
        "customer_id": {
            "bsonType": "objectId",
            },
        "room_id": {
            "bsonType": "objectId",
            },
        "cancel_status": {
            "bsonType": "bool",
            }
        }
    }         
}
