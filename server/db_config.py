import pymongo
from pymongo import MongoClient

class Database:  
  @staticmethod
  def connect_to_db():
    cluster=MongoClient("mongodb+srv://mongodb:mongodb@cluster0.uxi24a7.mongodb.net/?retryWrites=true&w=majority")
    db=cluster["hotel"]
    return db