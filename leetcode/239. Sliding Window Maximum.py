class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()#monotonically decreasing,max in a window
        n = len(nums)

        left = 0
        ans = []
        for right in range(n):
            #preserve decreasing
            while queue and nums[right] > queue[-1]:
                queue.pop()

            queue.append(nums[right])

            if right - left + 1 > k:
                left_ = nums[left]
                if left_ == queue[0]:
                    queue.popleft()
                left += 1
            if right-left+1 == k:
                ans.append(queue[0])
        return ans



        
        
