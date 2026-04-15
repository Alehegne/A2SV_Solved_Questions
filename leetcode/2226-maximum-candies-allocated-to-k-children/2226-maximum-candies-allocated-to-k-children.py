class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:





        # mn = min(candies)
        # if k > mn:
        #     return 0

        candies.sort()
        l,r = 1,candies[-1]

        def check(val):
            child = 0

            for cand in candies:
                child += cand // val
            return child >= k


        ans = 0
        while l <= r:
            mid = (l+r)//2

            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

        
        