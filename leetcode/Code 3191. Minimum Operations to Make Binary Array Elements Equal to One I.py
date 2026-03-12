class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ops = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                if i + 2 < n:
                    nums[i+1] ^= 1
                    nums[i+2] ^= 1
                    ops += 1
                else:
                    return -1
        return ops
        
