from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs):
        n = len(bombs)
        graph = defaultdict(list)

        # Build graph
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)

        # DFS
        def dfs(node, visited):
            visited.add(node)
            count = 1

            for nei in graph[node]:
                if nei not in visited:
                    count += dfs(nei, visited)

            return count

        ans = 0

        for i in range(n):
            ans = max(ans, dfs(i, set()))

        return ans
