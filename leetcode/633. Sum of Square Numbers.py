class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        l = 0
        r = int(math.isqrt(c))

        while l <= r:
            y = c - l*l
            sq = math.isqrt(y)
            if y == sq*sq:
                return True
            l += 1
        return False
            

        
