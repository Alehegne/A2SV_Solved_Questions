# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:



#         dirs = [[0,1],[0,-1],[1,0],[-1,0]]

#         row = len(heights)
#         col = len(heights[0])

#         def inbound(i,j):
#             return 0<=i<row and 0<=j<col


#         def dfs(i,j,visited,oc):


#             if i == 0 or j == 0:
#                 oc[0] = True
#             if i == row - 1 or j == col - 1:
#                 oc[1] = True
            
#             if oc[0] and oc[1]:
#                 return True
#             visited[i][j] = True

#             for rx,ry in dirs:
#                 new_r = i + rx
#                 new_c = j + ry

#                 if inbound(new_r,new_c) and \
#                 not visited[new_r][new_c] and \
#                 heights[new_r][new_c] <= heights[i][j]:
#                     res = dfs(new_r,new_c,visited,oc)

#                     if res:
#                         return True
#             return False
#         ans = []
#         for i in range(row):
#             for j in range(col):
#                 visited = [[False]*col for _ in range(row)]
#                 if dfs(i,j,visited,[False,False]):
#                     ans.append([i,j])
#         return ans


        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        if not heights:
            return []
        rows,cols = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()

        def inbound(x,y):
            return 0 <= x < rows and 0 <= y < cols
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x,y,visited):
            visited.add((x,y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if inbound(nx, ny) and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, visited)
        #left and right
        for r in range(rows):
            dfs(r, 0, pacific) 
            dfs(r, cols - 1, atlantic)
        #top and bottom
        for c in range(cols):
            dfs(0, c, pacific) 
            dfs(rows - 1, c, atlantic)
        # result = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) in pacific and (r, c) in atlantic:
        #             result.append([r, c])
        # return result
        return list(pacific.intersection(atlantic))


        
