import unittest
import prime

class Test_ISPrime(unittest.TestCase):
    def test_isprime(self):
        self.assertFalse(prime.isPrime(-1))
        self.assertFalse(prime.isPrime(0))
        self.assertFalse(prime.isPrime(1))
        self.assertTrue(prime.isPrime(2))
        self.assertTrue(prime.isPrime(17))
        self.assertTrue(prime.isPrime(19))
        self.assertFalse(prime.isPrime(21))


if __name__ == "__main__":
    unittest.main(False)    