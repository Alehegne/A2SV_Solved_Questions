class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort(reverse=True)

        amt = len(piles)//3
        sum_ = 0
        for i in range(1,amt*2,2):
            sum_ += piles[i]
        return sum_

        
