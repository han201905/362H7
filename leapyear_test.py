import unittest
from unittest import result
import leapyear

class Test(unittest.TestCase):
    def test_leap(self):
        result = leapyear.is_leap(2004)
        self.assertEqual(result, True)
    def test_2(self):
        result = leapyear.is_leap(2100)
        self.assertEqual(result, False)
    def test_3(self):
        result = leapyear.is_leap(2400)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()