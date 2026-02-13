class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


     
        p_w = {}
        w_p = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for p,c in zip(pattern,words):
            if p in p_w and p_w[p] != c or (c in w_p and w_p[c]!=p):
                return False
            if p not in p_w:
                p_w[p] = c
            if c not in w_p:
                w_p[c] = p
            # print(mapped)
        return True

        
