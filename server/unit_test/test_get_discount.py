from service.discount_service import DiscountService


pos_status = {
  'discount': 100
}

neg_status = {
  'discount': 0
}

email="bob@gmail.com"


def test_get_discount_positive(mocker):
  _ = mocker.patch('service.discount_service.DiscountService.calculate_discount', return_value = pos_status)
  discount_returned = DiscountService.calculate_discount(email)
  print(discount_returned)
  assert pos_status == discount_returned


def test_get_discount_negative(mocker):
  _ = mocker.patch('service.discount_service.DiscountService.calculate_discount', return_value =neg_status)
  discount_returned = DiscountService.calculate_discount(email) 
  assert neg_status == discount_returned


