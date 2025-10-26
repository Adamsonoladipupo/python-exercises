import unittest
from new_tuple import new_tuple

class TestNewTupleFunction(unittest.TestCase):
	def test_if_new_tuple_is_not_empty(self):
		expected = (1,2,3)
		actual = new_tuple(input = (1,2,3))
		self.assertEqual(actual, expected)
		
	def test_if_new_tuple_increase_tuple_length(self):
		before = (1,2,3)
		expected = (1,2,3,5,6)
		actual = new_tuple(before)
		self.assertTrue(len(actual) > expected)

