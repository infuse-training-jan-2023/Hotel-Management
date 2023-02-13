from service.customer_service import CustomerService

customer={

  "_id": {
    "$oid": "63e67417ba69fe385ca42d69"
  },
  "name": "harry",
  "email": "harry@gmail.com",
  "phone_number": "3696235689",
  "address": "margao goa"

}


def test_get_customer_makes_db_call(mocker):
  mock = mocker.patch('service.customer_service.CustomerService.get_customer', return_value = [])
  _ = CustomerService.get_customer(customer["email"])
  assert mock.call_count == 1

def test_get_customer(mocker):
  mock = mocker.patch('service.customer_service.CustomerService.get_customer', return_value = customer)
  customer_returned = CustomerService.get_customer(customer["email"])
  print(customer_returned)
#   for i, item in enumerate(customer_returned):
#     assert item == item[i]
  assert customer == customer_returned