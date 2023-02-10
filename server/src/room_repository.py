import pymongo
from pymongo import MongoClient
# from DB.init_db import connect_to_db

class RoomRepository:

  def __init__(self) -> None:   
    self.db = None


  def connect_db(self):
    if self.db is None:
      cluster=MongoClient("mongodb+srv://mongodb:mongodb@cluster0.uxi24a7.mongodb.net/?retryWrites=true&w=majority")
      self.db=cluster["hotel"]
      # self.db=connect_to_db()

  def get_room_details(self,room_no):
    try:
      self.connect_db()
      collection=self.db["room"]
      results= collection.find_one({"room_no": room_no})
      # print(results)
      # for result in results:
      #   print(result["name"])
      return results
    except Exception as e:
      raise Exception('Error: ', e)


