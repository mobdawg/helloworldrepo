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
        self.assertEqual(
            hl,
            ["hello world"],
            "hl object is empty list or having different string value composition",
        )

    def test_number_of_string_with_more_than_one_argument(self):
        itimes = 2
        hl = hellotext.helloworld_pythonic_func(itimes)
        self.assertEqual(itimes, len(hl))


class HelloTextCDerivedFuncTestCase(unittest.TestCase):
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

    def test_return_list_wuth_single_empty_string_argument(self):
        hl = hellotext.helloworld_derived_cfunc("")
        self.assertEqual(hl, [""], "hl value is referencing different object")

    def test_return_list_with_single_word_string_(self):
        hl = hellotext.helloworld_derived_cfunc("hello")
        self.assertEqual(
            hl,
            ["hello"],
            "hl object is empty list or having different string value only composition",
        )

    def test_if_true_the_returned_number_of_word_equal_to_argument_string(self):
        itimes = 2
        hl = hellotext.helloworld_derived_cfunc("hello", "world")
        self.assertTrue(itimes == len(hl))
