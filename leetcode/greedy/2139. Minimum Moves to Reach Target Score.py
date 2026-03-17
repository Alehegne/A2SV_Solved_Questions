class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        

        ans = 0
        while maxDoubles >= 0:
            if target == 1:
                break
            if maxDoubles == 0:
                ans += target - 1
                break
            elif target % 2 != 0:
                target -= 1
                ans += 1
            else:
                target //= 2
                maxDoubles -= 1
                ans += 1

        return ans
