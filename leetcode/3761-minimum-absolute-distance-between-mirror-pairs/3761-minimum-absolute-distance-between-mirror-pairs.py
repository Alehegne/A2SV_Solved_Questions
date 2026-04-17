class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:


        vis = {}
        ans = float('inf')

        for i,num in enumerate(nums):
            if num in vis:
                ans = min(ans,i-vis[num])
            vis[int(str(num)[::-1])] = i
        return ans if ans != float('inf') else -1




        