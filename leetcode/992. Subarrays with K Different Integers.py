class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        window = Counter()
        left = 0
        n = len(nums)
        count = 0
        prev = 0 #count the number of duplicate elements in the left

        for right,num in enumerate(nums):
            window[num] += 1
            #shrink if invalid
            if len(window) > k:
                while len(window) > k:
                    left_ = nums[left]
                    window[left_] -= 1
                    if window[left_] == 0:
                        del window[left_]
                    left += 1
                prev = 0
            # tp = left
            # tw = window.copy()
            # while len(tw) == k:
            #     count += 1
            #     lef = nums[tp]
            #     tw[lef] -= 1
            #     if tw[lef] == 0:
            #         del tw[lef]
            #     tp += 1
            while k == len(window) and window[nums[left]] > 1:
                prev += 1
                window[nums[left]] -= 1
                left += 1
            if k == len(window):
                count += prev + 1
        return count

        
                   
