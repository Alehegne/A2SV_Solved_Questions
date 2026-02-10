class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:


        ans = []
        sum_ = 0
        for num in nums:
            sum_ = sum_ + num if num % 2==0 else sum_
        for add,idx in queries:
            num = nums[idx]
            new = nums[idx] + add
            if num%2!=0 and new%2==0:
                sum_+=new
            elif num%2==0 and new % 2!=0:
                sum_-=num
            elif num % 2 == 0 and new % 2==0:
                sum_ += add
            ans.append(sum_)
            nums[idx]+=add
        return ans

            



        
