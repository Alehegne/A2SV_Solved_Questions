class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1,n):

            for j in range(m):
                left = matrix[i-1][j-1] if j - 1 >= 0 else float('inf')
                top = matrix[i-1][j]
                right = matrix[i-1][j+1] if j + 1 < m else float('inf')

                matrix[i][j] += min(left,top,right)
        return min(matrix[n-1])