class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        h_m = {}
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] not in h_m:
                h_m[s[i]] = i
        i = 0
        ans = []
        while i<len(s):
            las = h_m[s[i]]
            sub = s[i:las+1]
            j = las
            k = 1
            # for k in range(1,len(sub)):
            while k<len(sub):
                if h_m[sub[k]] > j:
                    sub += s[j+1:h_m[sub[k]]+1]
                    j = h_m[sub[k]]
                k += 1
            ans.append(j-i+1)
            i = j+1
        return ans


            









        
