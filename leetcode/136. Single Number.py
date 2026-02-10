class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        output = nums[0]
        for i in range(1,len(nums)):
            output ^=nums[i]
        return output

        
