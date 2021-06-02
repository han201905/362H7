import unittest
import FizzBuzz

class Test(unittest.TestCase):
    def test_false(self):
        result = FizzBuzz.fizzBuzz(9)
        self.assertEqual(result, "Fizz")


if __name__ == '__main__':
    unittest.main()