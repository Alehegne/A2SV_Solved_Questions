class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        def backtrack(path,i):
            if i == len(nums):
                ans.append(path[:])
                return
            #take
            backtrack(path+[nums[i]],i+1)
            #not take
            backtrack(path,i+1)

        backtrack([],0)
        return ans
