import unittest
from unittest import result
import FizzBuzz

class Test(unittest.TestCase):
    def test_false(self):
        result = FizzBuzz.fizzBuzz(9)
        self.assertEqual(result, "Fizz")
    
    def test_false(self):
        result = FizzBuzz.fizzBuzz(25)
        self.assertEqual(result, "Buzz")


if __name__ == '__main__':
    unittest.main()