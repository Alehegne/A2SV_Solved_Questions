class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_ = float("-inf")
        curr = 0

        for num in nums:
            curr = max(curr + num,num)
            max_ = max(curr,max_)
        return max_
        
