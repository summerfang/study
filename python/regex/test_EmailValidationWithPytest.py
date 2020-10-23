import pytest

from email_validation import is_email_valid

def test_is_email_valid():
    assert(is_email_valid("test@test.com"), True)