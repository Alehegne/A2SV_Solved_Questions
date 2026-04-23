class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        
        row = len(isConnected)
        vis = set()

        def dfs(i):

            vis.add(i)

            for neigh in range(row):
                if isConnected[i][neigh] == 1 and neigh not in vis:
                    dfs(neigh)
        ans = 0
        for i in range(row):
            if i not in vis:
                dfs(i)
                ans += 1
        return ans
        
