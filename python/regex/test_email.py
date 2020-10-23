# from email import is_email_valid
from email_validation import is_email_valid

def test_is_email_valid():
    emails = {
        "test@test.com": True,
        "test.test@test.com" : True,
        "test@test": False
    }


    for e in emails:
        if is_email_valid(e) == emails[e]:
            print("Valid")
        else:
            print("invalid")

test_is_email_valid()