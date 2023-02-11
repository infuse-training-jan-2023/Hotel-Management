addons_validator = {
    "$jsonSchema": {
    "bsonType": "object",
    "required": ["name", "price","id"],
    "properties":{
        "name": {
            "bsonType": "string",
            },
        "price": {
            "bsonType": "number",
            },
        "id": {
            "bsonType": "number",
            }
        }
    }         
}
