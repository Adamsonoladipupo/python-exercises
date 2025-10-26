import unittest
from unpacking_tuple import unpack

class TestUnpackingTupleFunction(unittest.TestCase):
	def test_if_unpack_function_unpacks_correctly(self):
		actual = unpack((1,2,3,4))
		expected = (1,2,[3,4])
		self.assertEqual(actual, expected)
		