class Solution:
    def numSquares(self, n: int) -> int:


        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1

            while j * j <= i:
                square = j * j
                dp[i] = min(dp[i], 1 + dp[i - square])
                j += 1

        return dp[n]
        


        # def dp(rem):
            
        #     if rem in memo:
        #         return memo[rem]

        #     if rem == 0:
        #         return 0
            
        #     if rem < 0:
        #         return float('inf')
            
        #     mn = float('inf')
        #     for i in range(1,int(rem**0.5) + 1):
        #         sq = i ** 2
        #         mn = min(mn,1 + dp(rem - sq))
        #     memo[rem] = mn
        #     return mn
        # memo = {}
        # return dp(n)


"""

CODE DAILY (:)
"""
