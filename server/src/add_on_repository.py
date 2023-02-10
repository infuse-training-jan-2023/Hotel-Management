import pymongo
from pymongo import MongoClient
# from DB.init_db import connect_to_db

class AddonRepository:

  def __init__(self) -> None:   
    self.db = None


  def connect_db(self):
    if self.db is None:
      cluster=MongoClient("mongodb+srv://mongodb:mongodb@cluster0.uxi24a7.mongodb.net/?retryWrites=true&w=majority")
      self.db=cluster["hotel"]
      # self.db=connect_to_db()

  def get_all_add_ons(self):
    try:
      self.connect_db()
      collection=self.db["add-ons"]
      results= collection.find({})
    #   for result in results:
    #     print(result["name"])
      return results
    except Exception as e:
      raise Exception('Error: ', e)


