class Solution:
    def minSteps(self, s: str, t: str) -> int:


        fs = Counter(s)
        ft = Counter(t)

        c = 0
        for k in fs.keys():

            diff = fs[k] - ft[k]
            if diff>0:
                c+=diff
        return c
        
