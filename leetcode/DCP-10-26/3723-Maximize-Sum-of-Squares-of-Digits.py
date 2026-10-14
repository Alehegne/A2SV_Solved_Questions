class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        

        ans = []
        for i in range(9,0,-1):
            d = sum // i

            sum -= d*i

            ans.extend([i]*d)
        rest = num - len(ans)
        ans.extend([0]*rest)
        if len(ans) != num:
            return ""
        return ''.join(map(str,ans))

