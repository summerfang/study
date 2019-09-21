import unittest
import prime

class Test_ISPrime(unittest.TestCase):
    def test_isprime(self):
        self.assertTrue(prime.isPrime(7))

if __name__ == "__main__":
    unittest.main(False)    