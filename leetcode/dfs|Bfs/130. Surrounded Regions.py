class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])
        visited = [[False]*m for _ in range(n)]

        dirs = [[0,-1],[0,1],[1,0],[-1,0]]



        def inbound(i,j):
            return 0<=i<n and 0<=j<m

        def dfs(i,j):
            if board[i][j] == "X":
                return

            visited[i][j] = True
            
            for rx,ry in dirs:
                new_r = rx + i
                new_c = ry + j
                if inbound(new_r,new_c) and not visited[new_r][new_c]:
                    dfs(new_r,new_c)

        #upper
        for i in range(m):
            if not visited[0][i]:
                dfs(0,i)
        #lower
        for i in range(m):
            if not visited[n-1][i]:
                dfs(n-1,i)
        #left
        for i in range(n):
            if not visited[i][0]:
                dfs(i,0)
        #right
        for i in range(n):
            if not visited[i][m-1]:
                dfs(i,m-1)

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j]=="O":
                    board[i][j] = "X"
        
