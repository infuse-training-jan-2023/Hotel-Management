from db_config import Database
from model.add_on import add_on_schema
class AddonService:
    @staticmethod
    def get_all_add_ons():
        db=Database.connect_to_db()

        collection=db["add-ons"]
        results= collection.find({})
        return results
