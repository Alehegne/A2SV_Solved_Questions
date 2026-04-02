class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:



        ans = []
        n = len(nums)
        taken = [False] * n
        nums.sort()

        def back(path,taken):
            if len(path) == n:
                ans.append(path[:])
                return
            
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1] and not taken[i-1]:
                       continue
                if not taken[i]:
                    taken[i] = True
                    back(path+[nums[i]],taken)
                    taken[i] = False
                                     
        back([],taken)
        return ans
        

        