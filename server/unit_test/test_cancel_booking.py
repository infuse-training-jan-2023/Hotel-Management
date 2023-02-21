from service.booking_service import BookingService
import pytest

bookingService = BookingService()

result = {"msg" : "booking canceled"}

def test_cancel_booking_makes_db_call(mocker):
  mock = mocker.patch('service.booking_service.BookingService.cancel_booking', return_value = [])
  _ = bookingService.cancel_booking()
  assert mock.call_count == 1


def test_cancel_booking(mocker):
    mock = mocker.patch('service.booking_service.BookingService.cancel_booking', return_value = result)
    msg_returned = bookingService.cancel_booking()
    assert result == msg_returned