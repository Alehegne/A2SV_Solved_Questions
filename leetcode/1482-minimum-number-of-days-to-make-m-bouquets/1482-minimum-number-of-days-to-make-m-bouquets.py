class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def can_make(days):
            b = 0
            f = 0
            for blm in bloomDay:
                if blm <= days:
                    f += 1
                    if f == k:
                        b += 1
                        f = 0
                else:
                    f = 0
            return b >= m
        left, right = min(bloomDay), max(bloomDay) 
        while left < right:
            mid = left + (right - left) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1
        return left
        