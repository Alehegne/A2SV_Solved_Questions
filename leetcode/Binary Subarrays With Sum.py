class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)
        vis = Counter({0:1})
        ps = 0
        count = 0
        
        for i,num in enumerate(nums):
            ps += num
            needed = ps - goal
            #ps2 - ps1 = goal
            if needed in vis:
                count += vis[needed]
            vis[ps] += 1
        return count
