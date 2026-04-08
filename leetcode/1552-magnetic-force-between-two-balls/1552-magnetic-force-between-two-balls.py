class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def check(apart):
            prev = position[0]
            placed = 1

            for i in range(1,len(position)):
                if position[i] - prev >= apart:
                    placed += 1
                    prev = position[i]
                    if placed == m:
                        break
            return placed >= m
        

        l ,r = 0,position[-1]

        ans = 0
        while l <= r:
            mid = l + (r-l)//2

            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
        