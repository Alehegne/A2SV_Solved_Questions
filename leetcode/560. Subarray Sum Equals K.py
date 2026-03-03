class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #greater shrink
        left = 0
        n = len(nums)
        pr = 0
        count = 0
        pr_map = {0:1}
        for right in range(n):
            pr += nums[right]
            if pr - k in pr_map:
                count += pr_map[pr-k]     
            pr_map[pr] = pr_map.get(pr,0) + 1      
        return count
            

        
