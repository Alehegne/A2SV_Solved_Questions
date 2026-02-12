class Solution:
    def frequencySort(self, s: str) -> str:


        f = Counter(s)
        s = sorted(f,key = lambda k: -f[k])
        ans = []
        for c in s:
            ans.append(c*f[c])
        return "".join(ans)

        
