class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        start = num//3 - 1
        ans = []
        if start*3+3==num:
            ans.extend([start,start+1,start+2])
        return ans
        
