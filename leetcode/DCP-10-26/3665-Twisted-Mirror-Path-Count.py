class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        

        dirs = [(0,1),(1,0)]
        n = len(grid)
        m = len(grid[0])

        def inbound(i,j):
            return 0 <= i < n and 0 <= j < m


        #brute-force
        #dr = 0 -> down, dr = 1 -> right
        MOD = 10**9 + 7
        @cache
        def dp(i,j,dr):

            if i == n - 1 and j == m - 1:
                return 1
            if not inbound(i,j):
                return 0
            
            if grid[i][j] == 1:
                if dr:
                    return dp(i+1,j,0)
                else:
                    return dp(i,j+1,1)

            local = 0
            for di,dj in dirs:
                nx,ny = di + i, dj + j
                d = dj == 1
                local += dp(nx,ny,d)
            return local % MOD
                
        return dp(0,0,None) % MOD


# 0 1 0
# 0 0 1
# 1 0 0

#0 1 1
#1 1 0