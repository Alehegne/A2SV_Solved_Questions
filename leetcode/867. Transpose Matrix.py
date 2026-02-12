class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
        # r = len(matrix)
        # c = len(matrix[0])
        # T = [[] for _ in range(c)]
        # for i in range(r):
        #     for j in range(c):
        #         T[j].append(matrix[i][j])
        # return T



