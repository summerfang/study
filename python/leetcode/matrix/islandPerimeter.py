from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Every cell: 1)touch border vs no touch. 2). touch other cell

        rows = len(grid)
        cols = len(grid[0])

        peri = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0: continue

                if row - 1 < 0: 
                    peri += 1
                else:
                    if grid[row - 1][col] == 0: peri += 1
                
                if row + 1 >= rows: 
                    peri += 1
                else:
                    if grid[row + 1][col] == 0: peri += 1

                if col - 1 < 0:
                    peri += 1
                else:
                    if grid[row][col - 1] == 0: peri += 1

                if col + 1 >= cols:
                    peri += 1
                else:
                    if grid[row][col + 1] == 0: peri += 1

        return peri
    
if __name__ == '__main__':
    s = Solution()

    # i = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    i = [[1]]
    print(s.islandPerimeter(i))