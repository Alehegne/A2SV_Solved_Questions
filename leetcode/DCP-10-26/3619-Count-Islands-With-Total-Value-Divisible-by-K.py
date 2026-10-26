class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        

        n = len(grid)
        m = len(grid[0])

        def inbound(i,j):
            return 0 <= i < n and 0 <= j < m
        

        def findSum(i,j):

            if not inbound(i,j):
                return 0
            if grid[i][j] == 0:
                return 0
            sm = grid[i][j]
            grid[i][j] = 0
            for xi,yi in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx,ny = i + xi,j+yi
                sm += findSum(nx,ny) 
            return sm
        

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    sm = findSum(i,j)
                    if sm % k == 0:
                        cnt += 1
        return cnt