class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n = len(mat)
        m = len(mat[0])

        dig = [[] for _ in range(n+m-1)]

        for r in range(n):
            for c in range(m):
                dig[r+c].append(mat[r][c])
        for i in range(len(dig)):
            if not i%2:
                dig[i].reverse()
        flatten = []
        for row in dig:
            flatten.extend(row)
        return flatten





        
