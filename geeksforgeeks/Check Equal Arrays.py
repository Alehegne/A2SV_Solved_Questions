from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        # return sorted(a)==sorted(b)
        a_f = Counter(a)
        b_f= Counter(b)
        for bk in b_f.keys():
            a_f[bk]-=b_f[bk]
            if a_f[bk] == 0:
                del a_f[bk]
            b_f[bk] = 0
        b_f=+b_f
        if len(a_f)>0 or len(b_f)>0:
            return False
        else:
            return True
            
a=[2,8,1]
b=[9,9,9]
sol=Solution()
print(sol.checkEqual(a,b))