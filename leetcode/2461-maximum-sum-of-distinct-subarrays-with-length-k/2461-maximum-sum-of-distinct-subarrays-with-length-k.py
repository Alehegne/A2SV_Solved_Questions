class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:


        vis = Counter(nums[:k])

        left = 0
        sm = sum(nums[:k])
        ans = 0
        for right in range(k,len(nums)):
            if k == len(vis):
                ans = max(sm,ans)
            vis[nums[right]] += 1
            sm += nums[right]
            sm -= nums[left]
            vis[nums[left]] -= 1
            if vis[nums[left]] == 0:
                del vis[nums[left]]
            left += 1
        if k == len(vis):
            ans = max(sm,ans)
        return ans


        