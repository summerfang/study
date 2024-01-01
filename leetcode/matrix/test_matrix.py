import pytest
from matrixReshape import Solution
from matrix import Matrix

@pytest.fixture
def mx_object():
    mx = Matrix()
    return mx

def test_matrixReshape():
    s = Solution()
    i = [[1,2],[3,4]]

    o = s.matrixReshape(i,4,1)
    assert [[1],[2],[3],[4]] == o

    o = s.matrixReshape(i,1,4)
    assert [[1,2,3,4]] == o

    i = [[1],[2],[3],[4]]
    o = s.matrixReshape(i, 2, 2)
    assert [[1,2],[3,4]] == o

def test_imageSmoother(mx_object):
    i = [[1,1,1],[1,0,1],[1,1,1]]
    assert mx_object.imageSmoother(i) == None