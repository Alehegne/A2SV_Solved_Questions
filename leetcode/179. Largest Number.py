class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def trimmed_leading_zero(n):
            res = ""
            for i,nn in enumerate(n):
                if nn != "0":
                    return n[i:]
            return "0"


        def compare_val(num1,num2):
            if (num1 + num2) < (num2 + num1):
                return True
            return False

        def sorted_(nums):
            for i in range(len(nums)):
                for j in range(len(nums)-i-1):
                    if compare_val(str(nums[j]),str(nums[j+1])):
                        nums[j],nums[j+1] = nums[j+1],nums[j] 
                    
        sorted_(nums)
        ans = "".join([str(num) for num in nums])
        
        trimmed = trimmed_leading_zero(ans)
        return trimmed
        



        
