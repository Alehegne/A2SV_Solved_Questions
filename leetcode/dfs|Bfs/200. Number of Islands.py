class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        n = len(grid)
        m = len(grid[0])
        # visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def dfs(row,col):
            grid[row][col] = "0"
            for rx,ry in directions:
                new_r = row + rx
                new_c = col + ry
                if inbound(new_r,new_c) and grid[new_r][new_c] == "1":
                    dfs(new_r,new_c)
        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    ans += 1
                    dfs(row,col)
        return ans
                


        
