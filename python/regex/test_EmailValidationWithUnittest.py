import unittest
from email_validation import is_email_valid

class Email_validation(unittest.TestCase):
    def setUp(self):
        self.emails =  {
        "test@test.com": True,
        "test.test@test.com" : True,
        "test@test": False
    }

    def test_is_email_valid(self):
        for email in self.emails:
            self.assertEqual(is_email_valid(email), self.emails[email])


if __name__ == '__main__':
   unittest.main()