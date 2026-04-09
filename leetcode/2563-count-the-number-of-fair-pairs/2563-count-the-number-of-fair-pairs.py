class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:


        nums.sort()
        ans = 0

        for i,num in enumerate(nums):

            left = bisect.bisect_left(nums,lower-num)
            right = bisect.bisect_right(nums,upper-num)

            ans += (max(right,i+1) - max(left,i+1))
        return ans
        