class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        

        given = Counter(nums)
        sum_ = 0
        ans = 0
        num = 1
        i = 0 #pointer on the given num
        while num <= n:
            if num not in given and sum_ < num:
                sum_ += num
                ans += 1 #patched
            if num in given:
                sum_ += num*given[num]
                i += given[num]
            while i < len(nums) and nums[i] <= sum_:
                sum_ += nums[i]
                i += 1
            num = sum_ + 1
        return ans
        
