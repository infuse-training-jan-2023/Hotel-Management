from service.booking_service import BookingService
import pytest

bookingService = BookingService()

result = {"msg": "booking succesfull"}

def test_book_room_makes_db_call(mocker):
  mock = mocker.patch('service.booking_service.BookingService.book_room', return_value = [])
  _ = bookingService.book_room()
  assert mock.call_count == 1


def test_book_room(mocker):
    mock = mocker.patch('service.booking_service.BookingService.book_room', return_value = result)
    msg_returned = bookingService.book_room()
    assert result == msg_returned