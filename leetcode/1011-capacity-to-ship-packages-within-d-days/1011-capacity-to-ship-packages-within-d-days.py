class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def valid(cap):
            day, curr = 1, 0
            for i,weight in enumerate(weights):
                if curr + weight > cap:
                    day += 1
                    curr = weight
                else:
                    curr += weight
                if day > days:
                    return False
            return True


        l = max(weights)
        r = sum(weights)
        ans = r

        while l <= r:

            md = (l+r)//2

            if valid(md):
                ans = md
                r = md - 1
            else:
                l = md + 1
        return ans
        