from service.booking_service import BookingService
import pytest

bookingService = BookingService()

result = [
    {
        "_id": {
            "$oid": "63e8990dd86932d6faf1e4d1"
        },
        "check_in": {
            "$date": "2023-02-25T00:00:00Z"
        },
        "check_out": {
            "$date": "2023-02-26T00:00:00Z"
        },
        "add_ons": [
            {
                "service": "gym",
                "price": 500
            },
            {
                "service": "break fast",
                "price": 700
            }
        ],
        "total_amount": 2200,
        "room_price": 1000,
        "customer_id": {
            "$oid": "63e6743305e14504ac5a50e3"
        },
        "room_id": {
            "$oid": "63e68ea543eefbbf88459d29"
        },
        "cancel_status": False
    },
    {
        "_id": {
            "$oid": "63e89a24955155fd981d0dd9"
        },
        "check_in": {
            "$date": "2023-02-26T00:00:00Z"
        },
        "check_out": {
            "$date": "2023-02-28T00:00:00Z"
        },
        "add_ons": [
            {
                "service": "break fast",
                "price": 200
            }
        ],
        "total_amount": 2200,
        "room_price": 1000,
        "customer_id": {
            "$oid": "63e6743305e14504ac5a50e3"
        },
        "room_id": {
            "$oid": "63e68ea543eefbbf88459d29"
        },
        "cancel_status": False
    }
    
]

email="bob@gmail.com"
def test_get_user_booking_makes_db_call(mocker):
  mock = mocker.patch('service.booking_service.BookingService.get_user_booking_by_email', return_value = [])
  _ = bookingService.get_user_booking_by_email(email)
  assert mock.call_count == 1


def test_get_user_booking_by_email(mocker):
    mock = mocker.patch('service.booking_service.BookingService.get_user_booking_by_email', return_value = result)
    msg_returned = bookingService.get_user_booking_by_email(email)
    assert result == msg_returned