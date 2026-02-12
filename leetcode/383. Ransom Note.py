class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:


        f = Counter(magazine)
        for c in ransomNote:
            if f[c] == 0:
                return False
            else:
                f[c]-=1
        return True
        
