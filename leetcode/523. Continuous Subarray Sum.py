class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ps = [0]*(n+1)
        for i in range(1,len(nums)+1):
            ps[i] += ps[i-1] + nums[i-1]
        rem_map = {0:0}#visited remainder map, fact:- if we number have the same remainder, their differece is divisible by k,rem:index
        print(ps)
        for i in range(1,len(ps)):
            rem = ps[i] % k
            if rem in rem_map and i-rem_map[rem] >= 2:
                return True
            if rem not in rem_map:
                rem_map[rem] = i
        return False


            

            





        
