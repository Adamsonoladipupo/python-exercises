import unittest
from transaction_app_function import *

class test_transaction_app_function(unittest.TestCase):
	def test_if_deposit_function_exits(self):
		deposit(amount =1, account_balance=1, transactions = [])
	
	def test_if_the_account_balance_increases(self):
		expected = 5000
		actual = deposit(amount = 5000, account_balance=0, transactions = [])
		self.assertEqual(actual,expected)