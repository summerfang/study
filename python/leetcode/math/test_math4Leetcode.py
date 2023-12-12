from math4Leetcode import Math4Leetcode
import pytest

@pytest.fixture
def math_obj():
    return Math4Leetcode()

@pytest.mark.parametrize("x, expected", [(121, True), (-121, False), (10, False)])

def test_isPalindrome(math_obj, x, expected):
    assert math_obj.isPalindrome(x) == expected


@pytest.mark.parametrize("x, expected", [('III',3)])
def test_romanToInt(math_obj, x, expected):
    assert math_obj.romanToInt(x) == expected