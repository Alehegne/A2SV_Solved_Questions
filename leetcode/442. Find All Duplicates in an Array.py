from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        idx = 0
        while idx < len(nums):
            while nums[nums[idx]-1] != nums[idx]:
                #swap
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]
            idx+=1
            # print("nums:",nums)
        ans = []
        # print(nums)
        for i in range(len(nums)):
            if i+1 != nums[i] and nums[i] == nums[nums[i]-1]:
                ans.append(nums[i])
        return ans
            
