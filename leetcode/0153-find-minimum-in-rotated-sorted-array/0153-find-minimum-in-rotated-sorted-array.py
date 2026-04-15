class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r = 0,len(nums)-1

        ans = nums[0]
        while l <= r:
            mid = (l+r)//2

            #increasing block
            if nums[l] <= nums[mid]:
                ans = min(ans,nums[l])
                l = mid + 1
            else:
                ans = min(ans,nums[mid])
                r = mid - 1
        return ans

        