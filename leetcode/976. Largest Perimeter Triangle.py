class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        def isValid(a,b,c):
            if a + b > c and b+c > a and a + c > b:
                return True
            else:
                return False
        max_ = 0
        for i in range(len(nums) - 3,-1,-1):
            a,b,c = nums[i],nums[i+1],nums[i+2]
            if isValid(a,b,c):
                return a + b + c
        return max_



        
