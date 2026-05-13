class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        min_heap = []
        for i in range(len(matrix)):
            heapq.heappush(min_heap,(matrix[i][0],i,0))
        
        for _ in range(k-1):
            el,row,col = heapq.heappop(min_heap)

            if col + 1 < len(matrix[0]):
                heapq.heappush(min_heap,(matrix[row][col+1],row,col+1))
        return min_heap[0][0]

        
        

        
