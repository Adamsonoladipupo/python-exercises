import unittest
from change_third_second import change_third_second

class TestChangeThirdSecondElement(unittest.TestCase):
	def test_if_change_third_second_is_not_empty(self):
		result = change_third_second(input = (1,2)
		self.assertTrue(len(result) > 0, "message")