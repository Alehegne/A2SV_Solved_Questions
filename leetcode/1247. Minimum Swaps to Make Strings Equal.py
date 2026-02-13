class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy,yx = 0,0

        for c1,c2 in zip(s1,s2):
            #x
            if c1 < c2:
                xy += 1
            elif c1 > c2:#y
                yx += 1
        if (xy + yx) % 2:
            return -1
        
        swap = xy//2 + yx//2
        return swap if not xy % 2 else swap + 2
