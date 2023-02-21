from DB.connect import Connection
import pymongo
class AddonService:
    @staticmethod
    def get_all_add_ons():
        try:
            results= Connection.db.add_ons.find({})
            return results
        except pymongo.errors.WriteError as e:
            raise Exception("Error:", e.__class__)
