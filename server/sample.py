from pymongo import MongoClient
import pymongo
from db_config import Database

db = Database.connect_to_db()

validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [ "name", "age" ],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "age": {
                "bsonType": "int",
                "minimum": 0,
                "maximum": 150,
                "description": "must be an integer between 0 and 150 and is required"
            }
        }
    }
}

db.create_collection('students', validator=validator)

document = {
    "name": "John Doe",
    "age": 25
}

db.students.insert_one({"nme" : "john"})
# try:
#     document.validate_collection()
# except pymongo.errors.CollectionInvalid as e:
#     print(e)
# validation_result = db.students.validate(document)
# validation_result=db.runCommand( { validate: "myCollection" } )

# print(validation_result)