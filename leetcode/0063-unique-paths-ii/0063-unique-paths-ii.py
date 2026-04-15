class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        total = [[0] * (m + 1) for _ in range(n+1)]

        for row in range(1,n+1):
            for col in range(1,m+1):
                if row != 1 or col != 1:
                    if obstacleGrid[row-1][col-1] == 1:
                        total[row][col] = 0
                    else:
                        total[row][col] = total[row-1][col] + total[row][col-1]
                else:
                    if obstacleGrid[row-1][col-1] == 1:
                        return 0
                    total[row][col] = 1
        print(total)
        return total[n][m]


        