class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = set()

        r = len(matrix)
        c = len(matrix[0])

        #position of the zero,
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zero.add((i,j))
        zero_ed_row = set()
        zero_ed_col = set()
        for i in range(r):
            for j in range(c):
                if (i,j) in zero:
                    #make the row and column zero
                    #single column
                    if j not in zero_ed_col:
                        for k in range(r):
                            matrix[k][j] = 0
                        zero_ed_col.add(j)
                    #single row
                    if i not in zero_ed_row:
                        for k in range(c):
                            matrix[i][k] = 0
                        zero_ed_row.add(i)


        
    
