from service.add_on_services import AddonService

add_ons=[
    {
        "name": "Spa",
        "price": 350
    },
    {
        "name": "Parking",
        "price": 100
    },
    {
        "name": "Breakfast",
        "price": 350
    },
    {
        "name": "Gym",
        "price": 150
    }
]

def test_get_all_add_ons_makes_db_call(mocker):
  mock = mocker.patch('service.add_on_services.AddonService.get_all_add_ons', return_value = [])
  _ = AddonService.get_all_add_ons()
  assert mock.call_count == 1

def test_get_all_add_ons_positive(mocker):
  mocker.patch('service.add_on_services.AddonService.get_all_add_ons', return_value = add_ons)
  add_ons_returned = AddonService.get_all_add_ons()
  assert add_ons == add_ons_returned


#   def test_get_all_add_ons_positive(mocker):
#   mocker.patch('pymongo.collection.Collection.find', return_value = add_ons)
#   add_ons_returned = AddonService.get_all_add_ons()
#   assert add_ons == add_ons_returned