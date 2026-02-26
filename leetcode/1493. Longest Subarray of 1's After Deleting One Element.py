class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

        left=0
        cnt=0
        max_=0

        for r,n in enumerate(nums):
            if nums[r] == 0:
                cnt+=1
            while cnt>1:
                if nums[left]==0:
                    cnt-=1
                left+=1
            max_=max(max_,r-left)
        return max_
