class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n = len(nums)
        MOD = 10**9 + 7
        ps = [0]*n
        for start,end in requests:
            ps[start] += 1
            if end + 1 <n:
                ps[end+1] -= 1
        for i in range(1,n):
            ps[i] += ps[i-1]
        nums.sort(reverse = True)
        ps.sort(reverse = True)
        res = 0
        for n,p in zip(nums,ps):
            res += n*p
        return res % MOD





        
