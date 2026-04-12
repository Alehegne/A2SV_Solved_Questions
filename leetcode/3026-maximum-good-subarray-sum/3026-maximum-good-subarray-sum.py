class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)

        pr = [0]*(n+1)

        for i in range(1,n+1):
            pr[i] = pr[i-1] + nums[i-1]
        # vis = defaultdict(list)

        # ans = float('-inf')

        # for i,num in enumerate(nums):
        #     if num - k in vis:
        #         for idx in vis[num-k]:
        #             ans = max(ans,pr[i+1] - pr[idx])
        #     if num + k in vis:
        #         for idx in vis[num+k]:
        #             ans = max(ans,pr[i+1] - pr[idx])

        #     vis[num].append(i)
        # return ans if ans != float('-inf') else 0
        vis = {}
        ans = float('-inf')
        for i,num in enumerate(nums):
            if num - k in vis:
                ans = max(ans,pr[i+1] - pr[vis[num-k]])
            if num + k in vis:
                ans = max(ans,pr[i+1] - pr[vis[num+k]])
            if (num in vis and pr[i] - pr[vis[num]] < 0) or num not in vis:
                vis[num] = i
        return ans if ans != float('-inf') else 0




        