class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # from itertools import permutations

        # perm = permutations(nums)
        # output = [list(per) for per in perm]
        # return output
        
        # def dfs(n):
        #     if len(n) == 1:
        #         return [n]
            
        #     result = []
        #     for i in range(len(n)):
        #         curr = n[i]
        #         rest = n[:i] + n[i+1:]
        #         for p in dfs(rest):
        #             p.append(curr)
        #             result.append(p)   
        #     return result

        # return dfs(nums)

        res = []
        curr = []
        def backtrack():

            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack()
                    curr.pop()
        backtrack()
        return res
        
