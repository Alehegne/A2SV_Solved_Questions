class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        graph = [[] for _ in range(numCourses)]
        for v,pre in prerequisites:
            graph[pre].append(v)
        
        indegree = [0] * numCourses

        for i in range(numCourses):
            for nei in graph[i]:
                indegree[nei] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []

        while queue:

            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []
        
