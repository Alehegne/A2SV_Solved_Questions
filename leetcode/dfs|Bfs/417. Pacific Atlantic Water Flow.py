class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:



        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        row = len(heights)
        col = len(heights[0])

        def inbound(i,j):
            return 0<=i<row and 0<=j<col


        def dfs(i,j,visited,oc):


            if i == 0 or j == 0:
                oc[0] = True
            if i == row - 1 or j == col - 1:
                oc[1] = True
            
            if oc[0] and oc[1]:
                return True
            visited[i][j] = True

            for rx,ry in dirs:
                new_r = i + rx
                new_c = j + ry

                if inbound(new_r,new_c) and \
                not visited[new_r][new_c] and \
                heights[new_r][new_c] <= heights[i][j]:
                    res = dfs(new_r,new_c,visited,oc)

                    if res:
                        return True
            return False
        ans = []
        for i in range(row):
            for j in range(col):
                visited = [[False]*col for _ in range(row)]
                if dfs(i,j,visited,[False,False]):
                    ans.append([i,j])
        return ans


        
