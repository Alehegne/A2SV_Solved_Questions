class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        import math
        row = len(matrix)
        col = len(matrix[0])
        if row==1:
            return [num for num in matrix[0]]
        elif col == 1:
            return [ele[0] for ele in matrix]
        i = 0
        vis = []
        n = row*col
        while i<row:
            if len(vis) == n:
                break
            #top
            for t in range(i,col - i):
                vis.append(matrix[i][t])
            #right
            for r in range(i+1,row-i):
                vis.append(matrix[r][col-i-1])
            #bottom
            if len(vis) == n:
                break
            for b in range(col-i-2,i-1,-1):
                vis.append(matrix[row-i-1][b])
            #left
            for l in range(row-i-2,i,-1):
                vis.append(matrix[l][i])
            i+=1


        return vis



        
