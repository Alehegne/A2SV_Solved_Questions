class Solution:
    def findValidPair(self, s: str) -> str:

        f = Counter(s)
        for i,n in enumerate(s):
            if i+1<len(s) and int(n)==f[n] and int(s[i+1])==f[s[i+1]] and int(n)!=int(s[i+1]):
                return f"{n}{s[i+1]}"
        return ""

        
