import unittest
import LeapYearFileTestDriven

class testcase2(unittest.TestCase):
    def test_IsNotLeapYear(self):
        result = LeapYearFileTestDriven.LeapYear(1700)
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()