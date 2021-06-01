import unittest
import FizzBuzz

class testcase2(unittest.TestCase):
    def test_multiples3(self):
        result = FizzBuzz.FizzFunc()
        self.assertEqual(result, 33)

    def test_multiples5(self):
        result = FizzBuzz.BuzzFunc()
        self.assertEqual(result, 20)
        
if __name__ == '__main__':
    unittest.main()