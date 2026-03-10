class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        left = 0
        min_ = deque()#increasin
        max_ = deque() #decreasing
        ans = 0

        for i,n in enumerate(nums):

            while max_ and n > max_[-1]:
                max_.pop()
            while min_ and n < min_[-1]:
                min_.pop()
            max_.append(n)
            min_.append(n)

            while max_ and min_ and max_[0] - min_[0] > limit:
                l = nums[left]
                if l == min_[0]:
                    min_.popleft()
                if l == max_[0]:
                    max_.popleft()
                left += 1
            ans = max(ans,i-left+1)
        return ans
            


        
