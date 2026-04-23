"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:


        graph = defaultdict(list)
        #1:[subordinate,importance]

        n = len(employees)
        for i in range(n):
            graph[employees[i].id] = [employees[i].subordinates,employees[i].importance]
        
        q = deque(graph[id][0])
        ans = graph[id][1]


        
        while q:

            idx = q.popleft()
            ans += graph[idx][1]

            q.extend(graph[idx][0])
        return ans



        
