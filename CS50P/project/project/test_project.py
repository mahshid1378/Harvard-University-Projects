import unittest
from project import greet_user, calculate_sum, is_even

class TestProject(unittest.TestCase):

    def test_greet_user(self):
        result = greet_user("John!")
        self.assertEqual(result, "Hello, John! How can I assist you today?")

    def test_calculate_sum(self):
        result = calculate_sum(2, 3)
        self.assertEqual(result, 5)

    def test_is_even(self):
        result1 = is_even(4)
        self.assertTrue(result1)

        result2 = is_even(7)
        self.assertFalse(result2)

if __name__ == '__main__':
    unittest.main()