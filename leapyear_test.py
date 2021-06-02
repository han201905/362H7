import unittest
import leapyear

class Test(unittest.TestCase):
    def test_leap(self):
        result = leapyear.is_leap(2004)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()