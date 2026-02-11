class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:


        n = len(changed)
        if n & 1:
            return []
        changed.sort()
        f = Counter(changed)
        h = []
        for num in changed:
            if f[num] == 0:
                continue
            f[num]-=1
            if num*2 in f and f[num*2]>0:
                h.append(num)
                f[num*2] -= 1 
            else:
                return []
        return h
        
