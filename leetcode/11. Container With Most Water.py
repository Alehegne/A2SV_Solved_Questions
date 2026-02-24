class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r = 0,len(height) - 1
        max_ = -inf
        while l < r:

            h = min(height[l],height[r])
            length = r - l
            max_ = max(max_,h*length)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_

        
