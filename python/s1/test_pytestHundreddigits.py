import pytest
from hundreddigits import *

def test_f1():
    a = getHundredDigits(1,1,1,1)
    assert a == 1

def test_f2():
    a = getHundredDigits(0,0,0,0)
    assert a == 0