import unittest
import FizzBuzz

class testcase2(unittest.TestCase):
    def test_multiples3(self):
        result = FizzBuzz.FizzFunc()
        self.assertEqual(result, 33)

    def test_multiples5(self):
        result = FizzBuzz.BuzzFunc()
        self.assertEqual(result, 20)

    def test_multiples3and5(self):
        result = FizzBuzz.FizzBuzzFunc()
        self.assertEqual(result, 6)
        
if __name__ == '__main__':
    unittest.main()