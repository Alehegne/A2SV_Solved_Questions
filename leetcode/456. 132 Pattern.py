class Solution:
    def find132pattern(self,nums:int)->bool:
    
        stack = [] # keeps track of 32 pattern
        currMin = nums[0]#holds previous minimum value to the left of j

        for j in range(1, len(nums)):
            while stack and nums[j] >= stack[-1][0]:
                stack.pop()
            if stack and nums[j] > stack[-1][1]:
                return True
            stack.append((nums[j], currMin))
            currMin = min(currMin, nums[j])
        return False
