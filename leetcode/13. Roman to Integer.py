class Solution:
    def romanToInt(self, s: str) -> int:

        maps = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"CM":900,"XC":90,"IV":4,"CD":400,"IX":9,"XL":40}

        num = 0
        i = 0
        while i<len(s):
            if i+1 < len(s) and s[i:i+2] in maps:
                num += maps[s[i:i+2]]
                i+=1
            else:
                num += maps[s[i]]
            i += 1
        return num
   



        
