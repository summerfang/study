from hundreddigits import *    # The code to test
import unittest   # The test framework

class Test_HundredDigits(unittest.TestCase):
    def test_f1(self):
        a = getHundredDigits(1,1,1,2)
        self.assertEqual(a, 4, "a should be 4")

    def test_f2(self):
        a = getHundredDigits(0,0,0,0)
        self.assertEqual(a, 0, "a should be 0")

if __name__ == "__main__":
    unittest.main(exit=False)    