class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        

        """

        """

        # n = len(colors)

        # graph = [[] for _ in range(n)]

        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # next_ = {
        #     "R":"B",
        #     "B":"W",
        #     "W":"R"
        # }
        
        # def check(curr_idx):
        #     # print("checking...",curr_idx)
        #     queue = deque([[curr_idx,-1]])
        #     visited = set()

        #     # for child in graph[curr_idx]:

        #     while queue:
        #         child_color = ""
        #         visited.add(curr_idx)
        #         # print(queue)
        #         for _ in range(len(queue)):
        #             curr_idx,parent_color = queue.popleft()

        #             if parent_color != -1 and colors[curr_idx] != next_[parent_color]:
        #                 return False
        #             if not child_color:
        #                 child_color = colors[curr_idx]
        #             else:
        #                 if child_color != colors[curr_idx]:
        #                     return False
        #             visited.add(curr_idx)
        #             # queue.append([child,colors[parent_idx]])
        #             for child in graph[curr_idx]:
        #                 if child not in visited:
        #                     queue.append([child,colors[curr_idx]])
        #     return True
        # for i in range(n):
        #     if check(i) and len(graph[i]) < 3:
        #         return i
        # return -1

        n = len(colors)

        # graph = [[] for _ in range(n)]
        indegree = [0]*n
        degree = [0] * n

        next_ = {
            "R":"B",
            "B":"W",
            "W":"R"
        }
        for u,v in edges:

            if colors[u] == colors[v]:
                return -1

            #  R -> B -> W ->R

            if colors[u] == next_[colors[v]]: # v -> u
                indegree[u] += 1
            else:
                indegree[v] += 1

            # graph[u].append(v)
            # graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        roots = [i for i in range(n) if indegree[i] == 0]
        print("roots:",roots)
        print(indegree)

        if len(roots) != 1:
            return -1
        
        if any(indegree[i] != 1 for i in range(n) if i != roots[0]):
            return -1
        
        return roots[0] if degree[roots[0]] < 3 else -1
        



