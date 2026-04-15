class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        total = [[0]*(n+1) for _ in range(m+1)]
        for r in range(1,m+1):
            for c in range(1,n+1):
                if c != 1 and r != 1:
                    total[r][c] = total[r-1][c] + total[r][c-1]
                else:
                    total[r][c] = 1
        return total[m][n]
        