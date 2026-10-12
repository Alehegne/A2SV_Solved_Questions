class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        

        @cache
        def dp(rem,i):

            if rem == 0:
                return 1
            if rem < 0 or i >= len(coins):
                return 0
            not_take = dp(rem,i+1)
            take = dp(rem-coins[i],i)

            return not_take + take
        return dp(amount,0)