class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = [-1] * len(graph)
        #-1 unvisited, 1-group1, 0-group2

        def can_color(i,curr_color):

            colors[i] = curr_color

            for nei in graph[i]:
                if colors[nei] != -1: #visited
                    if colors[nei] != 1-curr_color:
                        return False
                elif not can_color(nei,1-curr_color):
                    return False
            return True
            


        vis = set()
        for i in range(len(graph)):
            if colors[i] == -1 and not can_color(i,0):
                return False
        return True
        
