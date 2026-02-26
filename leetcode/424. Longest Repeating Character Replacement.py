class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window=Counter()
        seen=0
        max_freq=-inf
        left=0
        max_=-inf
        for r,c in enumerate(s):
            window[c]+=1
            seen+=1
            max_freq=max(window[c],max_freq)
            while seen-max_freq>k:
                l_c=s[left]
                window[l_c]-=1
                max_freq=max(window.values())
                left+=1
                seen-=1
            max_=max(max_,r-left+1)
        return max_
            

        
            

            



        
