import sys
sys.path.insert(0, './service')
from search_service import Room

class SearchController:
    def get_all_rooms(self, filters):
        try:
            room = Room.get_all_rooms(filters)
            return room
        except Exception as e:
            return str(e)

