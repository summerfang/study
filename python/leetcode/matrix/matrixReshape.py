
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        x = len(mat)
        y = len(mat[0])
        if r * c != x * y:
            return mat
        
        new_mat = [[0 for row in range(c)] for col in range(r)]

        for i in range(x):
            for j in range(y):
                pos = i * y + j
                new_mat[pos//c][pos%c] = mat[i][j]
        return new_mat

if __name__ == '__main__':
    s = Solution()
    i : List[List[int]] = [[1,2],[3,4]]

    o = s.matrixReshape(i,4,1)
    print(o)

    o = s.matrixReshape(i,1,4)
    print(o)

    i : List[List[int]] = [[1],[2],[3],[4]]
    o = s.matrixReshape(i, 2, 2)
    print(o)