import unittest
import prime

class Test_ISPrime(unittest.TestCase):
    def test_isprime(self):
        self.assertTrue(prime.isPrime(7))
        self.assertFalse(prime.isPrime(-7))
        self.assertFalse(prime.isPrime(0))
        self.assertFalse(prime.isPrime(1))


if __name__ == "__main__":
    unittest.main(False)    