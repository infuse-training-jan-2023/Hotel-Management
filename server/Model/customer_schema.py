customer_validator = {
    "$jsonSchema": {
    "bsonType": "object",
    "required": ["name", "email","phone_number","address"],
    "properties":{
        "name": {
            "bsonType": "string",
            },
        "email": {
            "bsonType": "string",
            "pattern": "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            },
        "phone_number": {
            "bsonType": "string",
            "pattern": "^\d{10}$"
            },
        "address": {
            "bsonType": "string",
            }
        }
    }         
}
