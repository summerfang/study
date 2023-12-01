import pytest
from fibonacci import fib
from catalan import catalan, catalan_v2


def test_fib():
    verify_points = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
                     89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    
    for i in range(len(verify_points)):
        assert fib(i) == verify_points[i]


def test_catalan():
    verify_points = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786]
    
    for i in range(len(verify_points)):
        assert catalan(i) == verify_points[i]

def test_catalan_v2():
    verify_points = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786]
    
    for i in range(len(verify_points)):
        assert catalan_v2(i) == verify_points[i]