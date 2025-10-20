import unittest
from MFDS_function import *

class testing_multi_fuel_dispenser_system(unittest.TestCase):
	def test_if_buy_petrol_function_with_price_exit(self):
		buy_petrol_with_price(price= 500)

	def test_if_buy_petrol_function_with_price_return_the_correct_liter_value(self):
		expected = 700/650
		actual = buy_petrol_with_price(price= 700)
		self.assertEqual(actual, expected)

	def test_if_buy_petrol_function_with_liter_exit(self):
		buy_petrol_with_liter(liter= 500)

	def test_if_buy_petrol_function_with_liter_return_the_correct_price_value(self):
		expected = 700*650
		actual = buy_petrol_with_liter(liter= 700)
		self.assertEqual(actual, expected)
