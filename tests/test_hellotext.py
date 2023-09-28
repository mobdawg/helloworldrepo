import unittest
import hellotext


class HelloTextPythonicTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("class based setup for the entire test case")

	@classmethod
	def teadDownClass(cls):
		print("class based tear down cleanup for the entire test case")

	def setUp(self):
		print("setup for each test item")

	def tearDown(self):
		print("tear down cleanup for each test item")

	def test_return_empty_list_with_zero_value_argument(self):
		hl = hellotext.helloworld_pythonic_func(0)
		self.assertEqual(hl, [], "hl value is referencing different object")

	def test_return_list_of_words_with_default_argument(self):
		hl = hellotext.helloworld_pythonic_func()
		self.assertEqual(hl, ['hello world'], "hl object is empty list or having different string value composition")
