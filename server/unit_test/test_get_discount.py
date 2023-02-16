from service.booking_service import BookingService

booking={
  "_id": {
    "$oid": "63ea0a2a75a84883f4662ee0"
  },
  "check_in": {
    "$date": "2023-02-08T00:00:00Z"
  },
  "check_out": {
    "$date": "2023-02-15T00:00:00Z"
  },
  "add_ons": [
    {
      "service": "break fast",
      "price": 200
    }
  ],
  "total_amount": 14200,
  "room_price": 2000,
  "customer_id": {
    "$oid": "63e670f601343886816b44c7"
  },
  "room_id": {
    "$oid": "63e68ea543eefbbf88459d29"
  },
  "cancel_status": False,
  "guest_name": "bob dsouza",
  "email": "bob@gmail.com",
  "phone_number": "1234653789",
  "special_request": "required valet"
}

pos_status = {
  'discount': 10
}

neg_status = {
  'discount': 0
}

email="bob@gmail.com"


def test_get_discount_positive(mocker):
  mock = mocker.patch('service.booking_service.BookingService.calculate_discount', return_value = pos_status)
  discount_returned = BookingService.calculate_discount(email)
  print(discount_returned)
  assert pos_status == discount_returned


def test_get_discount_negative(mocker):
  mock = mocker.patch('service.booking_service.BookingService.calculate_discount', return_value =neg_status)
  discount_returned = BookingService.calculate_discount(email) 
  assert neg_status == discount_returned


