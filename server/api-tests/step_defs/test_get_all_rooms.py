import pytest
from pytest_bdd import scenarios, when, then
import requests, os
from dotenv import load_dotenv
from main import app
app=app.test_client()
load_dotenv() 
scenarios('../features/get_all_rooms.feature')

search_url = os.getenv("url")+"/rooms"

status = [{"_id": {"$oid": "63e68ea543eefbbf88459d29"}, "room_no": 101, "room_type": "single", "price": 2000, "capacity": 1, "amenities": ["tv", "speaker", "wifi"], "images": ["https://images.pexels.com/photos/271624/pexels-photo-271624.jpeg", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "When traveling on business, there is nothing more rewarding, than a comfortable room to come back to. All rooms are guaranteed to make your stay comfortable. Each room, has been meticulously furnished to standards that will exceed your expectations.", "title": "Standard single room with balcony view"}, {"_id": {"$oid": "63ea04adcf0530963faef92e"}, "room_no": 102, "room_type": "double", "price": 3000, "capacity": 3, "amenities": ["couch", "jacuzzi"], "images": ["https://images.pexels.com/photos/1743231/pexels-photo-1743231.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "Additional space to unwind in after a tiring day of attending to business. The deluxe rooms are fitted with twin beds and gives you a few extra sq. feet to just stretch yourself and relax.", "title": "Spacious premium double room "}, {"_id": {"$oid": "63ea04adcf0530963faef92f"}, "room_no": 201, "room_type": "double", "price": 2500, "capacity": 3, "amenities": ["water", "wifi", "ac"], "images": ["https://images.pexels.com/photos/14175921/pexels-photo-14175921.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "Additional space to unwind in after a tiring day of attending to business. The deluxe rooms are fitted with twin beds and gives you a few extra sq. feet to just stretch yourself and relax.", "title": "A simple minimal furnished double room"}, {"_id": {"$oid": "63ea04adcf0530963faef930"}, "room_no": 202, "room_type": "single", "price": 1200, "capacity": 2, "amenities": ["tv", "couch"], "images": ["https://images.pexels.com/photos/164595/pexels-photo-164595.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "When traveling on business, there is nothing more rewarding, than a comfortable room to come back to. All rooms are guaranteed to make your stay comfortable. Each room, has been meticulously furnished to standards that will exceed your expectations.", "title": "A cozy single room with sunset view"}, {"_id": {"$oid": "63ea04adcf0530963faef931"}, "room_no": 203, "room_type": "penthouse", "price": 8000, "capacity": 2, "amenities": ["jacuzzi", "wine", "speaker", "tv", "ac"], "images": ["https://images.pexels.com/photos/4915547/pexels-photo-4915547.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "At 5,000 square feet, this penthouse suite at the new view, a Luxury Collection Hotel, in Milan is the largest suite in India and it may also be the country's most sumptuous with glitzy Art Deco-inspired d\u00e9cor and precious materials like marble and crystal gracing nearly every surface. The white and gold living room with slanted reflecting walls features some of the most iconic Italian furnishings like mushroom-shaped Atollo table lamps, and brilliant white Chesterfield sofas by Fendi.", "title": "A grand space for a lavish stay at this Penthouse"}, {"_id": {"$oid": "63ea04adcf0530963faef932"}, "room_no": 301, "room_type": "single", "price": 3000, "capacity": 2, "amenities": ["tv"], "images": ["https://images.pexels.com/photos/6480198/pexels-photo-6480198.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "When traveling on business, there is nothing more rewarding, than a comfortable room to come back to. All rooms are guaranteed to make your stay comfortable. Each room, has been meticulously furnished to standards that will exceed your expectations.", "title": "A single room overlooking the city "}, {"_id": {"$oid": "63ea04adcf0530963faef933"}, "room_no": 302, "room_type": "double", "price": 1800, "capacity": 3, "amenities": ["water", "wine", "ac", "couch"], "images": ["https://images.pexels.com/photos/2635038/pexels-photo-2635038.jpeg?cs=srgb&dl=pexels-terry-magallanes-2635038.jpg&fm=jpg&w=1920&h=1282 ", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "Additional space to unwind in after a tiring day of attending to business. The deluxe rooms are fitted with twin beds and gives you a few extra sq. feet to just stretch yourself and relax.", "title": "A large double room with a pool view "}, {"_id": {"$oid": "63ea04adcf0530963faef934"}, "room_no": 303, "room_type": "single", "price": 1200, "capacity": 2, "amenities": ["couch", "jacuzzi"], "images": ["https://images.pexels.com/photos/271618/pexels-photo-271618.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", "https://images.pexels.com/photos/2082087/pexels-photo-2082087.jpeg?cs=srgb&dl=pexels-dmitry-zvolskiy-2082087.jpg&fm=jpg&w=1920&h=1281", "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?cs=srgb&dl=pexels-jean-van-der-meulen-1457842.jpg&fm=jpg&w=1920&h=1165"], "description": "When traveling on business, there is nothing more rewarding, than a comfortable room to come back to. All rooms are guaranteed to make your stay comfortable. Each room, has been meticulously furnished to standards that will exceed your expectations.", "title": "Garden facing single room"}]

@when('i try to search for room')
def get_rooms():
  pytest.api_response = app.get(search_url)

@then('i should get the rooms available based on filters')
def get_room_info():
  body = pytest.api_response.get_json()
  print(type(body))
  assert body[0]["_id"] == status[0]["_id"]

@then('the api status code should be 200')
def check_status_code():
  assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def validate_content_type():
  assert pytest.api_response.headers['Content-type'] == 'application/json'