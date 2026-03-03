class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pr = [1]*n
        sf = [1]*n
        pr[0] = nums[0]
        for i in range(1,n):
            pr[i] *= pr[i-1] * nums[i]
        sf[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            sf[i] *= sf[i+1]*nums[i]
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(sf[1])
                continue
            if i == n - 1:
                ans.append(pr[-2])
                continue
            ans.append(pr[i-1]*sf[i+1])
        return ans
        
