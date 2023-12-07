import pytest

from number import is_number, is_real_number

def test_is_number():
    test_data = [('0100',True),
                 ('',False),
                 ('100', True)]
    
    for k,v in test_data:
        assert is_number(k) == v


def test_is_real_number():
    test_data = [('0100',True),
                 ('',False),
                 ('100', True)]
    
    for k,v in test_data:
        assert is_real_number(k) == v