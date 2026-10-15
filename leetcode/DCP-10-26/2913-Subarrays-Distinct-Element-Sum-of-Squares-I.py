class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        

        ans = 0

        for i in range(len(nums)):

            dis = set([nums[i]])
            ans += 1
            for j in range(i+1,len(nums)):
                dis.add(nums[j])
                ans += len(dis) ** 2
        return ans
