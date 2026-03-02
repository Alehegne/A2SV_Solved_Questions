class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prefix_sum = [[0]*(m+1) for _ in range(n+1)]
        
        for row in range(n):
            for col in range(m):
                pr_r = row + 1
                pr_c = col + 1
                self.prefix_sum[pr_r][pr_c ] = matrix[row][col] +  self.prefix_sum[pr_r-1][pr_c] +  self.prefix_sum[pr_r][pr_c-1] - self.prefix_sum[pr_r-1][pr_c-1]

        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r_1 = row1 + 1
        r_2 = row2 + 1
        c_1 = col1 + 1
        c_2 = col2 + 1
        sum_ = self.prefix_sum[r_2][c_2] - self.prefix_sum[r_1-1][c_2] - self.prefix_sum[r_2][c_1-1] + self.prefix_sum[r_1-1][c_1-1]
        return sum_
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
