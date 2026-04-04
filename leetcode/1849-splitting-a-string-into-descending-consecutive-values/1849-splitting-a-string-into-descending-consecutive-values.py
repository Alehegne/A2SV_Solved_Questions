class Solution:
    def splitString(self, s: str) -> bool:


        ans = False

        def backtrack(start,prev,path):
            nonlocal s
            nonlocal ans

            if start == len(s) and len(path) > 1:
                f = True
                for i in range(1,len(path)):
                    if int(path[i]) - int(path[i-1]) != -1:
                        f = False
                        break
                ans = f
                return

    
            for i in range(start,len(s)):
                curr = s[start:i+1]
                if prev:
                    if int(curr) > int(prev):
                        break
                    if int(prev) - int(curr) > 1:
                        continue
                path.append(curr)
                backtrack(i+1,curr,path)
                path.pop()
        backtrack(0,None,[])
        return ans




            