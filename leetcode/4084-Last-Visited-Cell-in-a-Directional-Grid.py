class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:



        n = len(grid)
        m = len(grid[0])

        visited = [[False]*m for _ in range(n)]

        def valid(i,j):
            return 0<=i<n and 0<=j<m

        dir = {
            "L":(0,-1),
            "R":(0,1),
            "U":(-1,0),
            "D":(1,0)
        }
        visited[0][0] = True
        r,c = 0,0
        while True:

            dx,dy = dir[grid[r][c]]
            nx,ny = r + dx,c + dy

            if not valid(nx,ny) or visited[nx][ny]:
                break
            
            r,c = nx,ny
            visited[nx][ny] = True
            # print(r,c)

            
        return [r,c]

                            
            