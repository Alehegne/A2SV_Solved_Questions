class Solution:
       def combinationSum2(self,candidates, target):
            result = []
            n = len(candidates)
            candidates.sort()

            def backtrack(start, tar,path):
                nonlocal result
                if tar == 0:
                    result.append(path[:])
                for i in range(start, n):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    if candidates[i] > tar:
                        break
                    path.append(candidates[i])
                    backtrack(i + 1, tar - candidates[i],path) # move to the next index since we can't reuse same element
                    path.pop()
            backtrack(0,target,[])
            return result
        