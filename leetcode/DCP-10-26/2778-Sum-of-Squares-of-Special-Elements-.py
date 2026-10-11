class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        

        def factors(n):

            fact = set()
            fact.add(1)
            fact.add(len(nums))
            for i in range(2,int(n/2) + 1):

                if n % i == 0:
                    fact.add(i)
                    if n % (2*i) == 0:
                       fact.add(2*i)
            return fact
        
        ans = 0

        # print(factors(len(nums)))
        for n in factors(len(nums)):
            n -= 1
            if n == len(nums):  continue
            ans += (nums[n] ** 2)
        return ans


