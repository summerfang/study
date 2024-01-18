from math4Leetcode import Math4Leetcode
import pytest

@pytest.fixture
def math_obj():
    return Math4Leetcode()

@pytest.mark.parametrize("x, expected", [(121, True), (-121, False), (10, False)])

def test_isPalindrome(math_obj, x, expected):
    assert math_obj.isPalindrome(x) == expected


@pytest.mark.parametrize("x, expected", [('III',3), ('MCMXCIV',1994), ('LVIII',58)])
def test_romanToInt(math_obj, x, expected):
    assert math_obj.romanToInt(x) == expected

@pytest.mark.parametrize('x, expected', [([9],[1,0]), ([4,3,2,1],[4,3,2,2]), ([1,2,3],[1,2,4])])
def test_plus(math_obj, x, expected):
    assert math_obj.plusOne(x) == expected

@pytest.mark.parametrize('x, expected', [('bb', 2)])
def test_longestPalindrome(math_obj, x, expected):
    assert math_obj.longestPalindrome(x) == expected

@pytest.mark.parametrize('x, y, expected', [([1,2,3],[1,1],1)])
def test_findContentChildren(math_obj, x, y, expected):
    assert math_obj.findContentChildren(x, y) == expected

@pytest.mark.parametrize('x, expected', [([1,4,3,2], 4)])
def test_arrayPairSum(math_obj, x, expected):
    assert math_obj.arrayPairSum(x) == expected