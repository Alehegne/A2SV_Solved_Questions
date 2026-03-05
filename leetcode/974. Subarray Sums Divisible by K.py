class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        ps = [0]*n
        ps[0] = nums[0]
        for i in range(1,n):
            ps[i] += ps[i-1] + nums[i]
        rem_map = Counter()
        rem_map[0] = 1
        count = 0
        for s in ps:
            rem = s % k
            if rem in rem_map:
                count += rem_map[rem]
            rem_map[rem] += 1
            # print("s:",s,count,rem_map)
        return count
        
