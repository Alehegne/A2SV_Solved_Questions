from heapq import heappop,heappush
class Solution:
    def furthestBuilding(self, heights, bricks, ladders):

        n = len(heights)

        """
        bricks or ladders

        plan:
          - insight:- its is always optimal to use ladders for higher height that bricks, so
          i will greedily use ladders for long heights and then bricks
          - check is it possible to reach an index
          - max heap of height
          - O(n) for traversing, and O(n) for checking possibility to reach there:- O(n^2logn)
        #optimization
          1. only the sum is necessary for brick checking
          2. only the number of max is necessary for ladder checking
        #another round of thinking
        - for ladders, take top ladders max with in a min-heap
        - take the running sum of heights
        #bottleneck: getting the sum of k max num
        - solution:- only the heights with brick is necessary
        - bricks_sum
        - total_sum

        - add the popped to the bricks_sum

        - continue until bricks_sum is < avail bricks
        """

        

        with_ladders = []
        with_bricks = 0 
        for i in range(1,len(heights)):
            height_diff = heights[i] - heights[i-1]
            if height_diff > 0:
                heappush(with_ladders,height_diff)
            
            if len(with_ladders) > ladders:
                with_bricks += heappop(with_ladders)
            
            if with_bricks > bricks:
                return i - 1
        return n - 1




