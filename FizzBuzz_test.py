import unittest
from unittest import result
import FizzBuzz

class Test(unittest.TestCase):
    def test_1(self):
        result = FizzBuzz.fizzBuzz(9)
        self.assertEqual(result, "Fizz")
    
    def test_2(self):
        result = FizzBuzz.fizzBuzz(25)
        self.assertEqual(result, "Buzz")

    def test_3(self):
        result = FizzBuzz.fizzBuzz(30)
        self.assertEqual(result, "FizzBuzz")


if __name__ == '__main__':
    unittest.main()