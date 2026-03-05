class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0]*n
        ps[0] = nums[0]
        for i in range(1,n):
            ps[i] += ps[i-1] + nums[i]
        min_ = min(ps)
        return 1 - min_ if min_ < 0 else 1
        
