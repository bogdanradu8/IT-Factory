import unittest
from functions_tema08 import is_prime

class FunctionsTestCase(unittest.TestCase):
    def test_is_prime(self):
        expected_result = True
        actual_result = is_prime(7)

        self.assertIsInstance(actual_result, bool)
        self.assertEqual(expected_result, actual_result)
