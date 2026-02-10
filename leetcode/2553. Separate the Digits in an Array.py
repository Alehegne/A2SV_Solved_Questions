class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def getDigit(num):
            digit = []
            while num > 0:
                rem = num % 10
                digit.append(rem)
                num = int(num / 10)
            return digit[::-1]


        ans = []
        for num in nums:
            digits = getDigit(num)
            ans.extend(digits)
        return ans


        
