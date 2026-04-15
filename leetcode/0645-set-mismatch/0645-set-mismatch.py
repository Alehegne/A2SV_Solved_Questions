class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        ans = []

        for num in nums:
            p = abs(num)
            if nums[p-1] < 0:
                ans.append(p)
            if nums[p-1] > 0:
                nums[p-1] = -nums[p-1]
        dup = 0
        for i,num in enumerate(nums):
            if num > 0:
                dup = i
                break
        ans.append(i+1)
        return ans
        