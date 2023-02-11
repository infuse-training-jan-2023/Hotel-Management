review_validator = {
    "$jsonSchema": {
    "bsonType": "object",
    "required": ["rating", "feedback","customer_name","room_id"],
    "properties":{
        "rating": {
            "bsonType": "number",
            },
        "feedback": {
            "bsonType": "string",
            },
        "customer_name": {
            "bsonType": "string",
            },
        "room_id": {
            "bsonType": "objectId",
            }
        }
    }         
}
