class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        return len(list(grid[r][c] for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c]<0))
