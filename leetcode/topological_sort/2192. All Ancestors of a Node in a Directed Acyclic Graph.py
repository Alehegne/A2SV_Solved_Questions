class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)

        ans = [[] for _ in range(n)]

        # def dfs(start,current):
        #     # print("start:",start,vis,current)

        #     # if start in vis:
        #     #     return
        #     if start != current:
        #         if current not in ans[start]:
        #             ans[start].append(current)
            
        #     # vis.add(start)
        #     for nei in graph[start]:
        #         dfs(nei,current)
                
        
        # for i in range(n):
        #     dfs(i,i)
        # # print(ans)
        # return 
        

        #with top sort
        indegree = [0] * n
        for i in range(n):
            for idx in graph[i]:
                indegree[idx] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:

            node = queue.popleft()
            extend = [node] + ans[node]

            for nei in graph[node]:
                ans[nei].extend(extend)
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        for i in range(len(ans)):
            ans[i] = sorted(set(ans[i]))
            
        return ans





        
