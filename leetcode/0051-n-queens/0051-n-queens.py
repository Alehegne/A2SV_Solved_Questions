class Solution:
    def solveNQueens(self,n):
        def is_valid(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                    return False
            return True
        def backtrack(board, row):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'
        result = []
        board = [['.'] * n for _ in range(n)]
        backtrack(board, 0)
        return result