class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        n = len(board)
        m = len(board[0])

        inbound = lambda i,j: 0<=i<n and 0<=j<m

        dir_ = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = False
        

        def dfs(i, r, c):
            nonlocal ans

            if i == len(word):
                ans = True
                return
            
            if not inbound(r,c):
                return
            if word[i] != board[r][c]:
                return

            temp = board[r][c]
            board[r][c] = "#"
            for x, y in dir_:
                dfs(i+1, r+x, c+y)
            board[r][c] = temp
        for row in range(n):
            for col in range(m):
                dfs(0,row,col)
                if ans:
                    break
        return ans


        

        