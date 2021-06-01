import unittest
import LeapYearFileTestDriven

class testcase2(unittest.TestCase):
    def test_IsNotLeapYear(self):
        result = LeapYearFileTestDriven.LeapYear(1700)
        self.assertEqual(result, False)

    def test_IsLeapYear(self):
        result = LeapYearFileTestDriven.LeapYear(2000)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()