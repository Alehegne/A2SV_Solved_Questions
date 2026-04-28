class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = []
        n = len(graph) - 1

        def dfs(start,path):
            if start == n:
                ans.append(path[:] + [start])
                return
            path.append(start)
            for nei in graph[start]:
                dfs(nei,path)
            path.pop()
        dfs(0,[])
        return ans


        
