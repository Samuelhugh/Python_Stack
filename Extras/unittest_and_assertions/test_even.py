# Import Python Testing Framework
import unittest

# My "unit" - I will be running my tests on
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# My "unit tests" - Initialized by creating a class that inherit from unittest.TestCase
class IsEvenTests(unittest.TestCase):
# Each method in this class is a test to be run
    def test_one(self):
# Using assertEqual() here
        self.assertEqual(is_even(2), True)
# Another way to write above is
        self.assertTrue(is_even(2))
# Second test
    def test_two(self):
# Using assertEqual() again - Functions/Assertions
        self.assertEqual(is_even(3), False)
# Another way to write the above is - using assertFalse() here
        self.assertFalse(is_even(3))

# Any task I want ran before any method above is executed, put in setUp() method
    def setUp(self):
# Just printing something for now
        print("Running setUp")

# Any task I want ran after the tests are executed, put in tearDown method
    def tearDown(self):
# Just printing something for now
        print("Running tearDown tasks")

# Important for running test cases correctly
if __name__ == "__main__":
# This runs my tests
    unittest.main()