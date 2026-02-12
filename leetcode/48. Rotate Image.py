class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r = len(matrix)
        c = len(matrix[0])
        changed = set()
        for i in range(r):
            for j in range(c):
                #swap to get the transpose
                if (i,j) not in changed:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                    changed.add((j,i))
        for mat in matrix:
            mat.reverse()
        
