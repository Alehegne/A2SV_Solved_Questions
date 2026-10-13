class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        

        # nums.sort(key = lambda x:abs(x))
        # print(nums)


        # right , left = len(nums) - 1, 0
        # ans = 0
        # while left < right:

        #     ans += (nums[right] ** 2 - nums[left] ** 2)
        #     left += 1
        #     right -= 1
        # if len(nums) % 2:
        #     ans += nums[left] ** 2
        # return ans

        sq = sorted([x * x for x in nums])

        k = len(nums)//2

        return sum(sq[k:]) - sum(sq[:k])

"""
Code Lab :)
"""