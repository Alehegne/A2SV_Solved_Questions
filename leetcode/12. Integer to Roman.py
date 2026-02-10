class Solution:
    def intToRoman(self, num: int) -> str:
        maps = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        
        digits = [int(d) for d in str(num)]
        n = len(digits) - 1 #for place value
        roman = []
        for i in range(len(digits)):

            val = digits[i]*(10**n)

            if val in maps:
                roman.append(maps[val])
            else:
                if val > 1000:
                    roman.append(digits[i]*maps[1000])
                elif val > 500:
                    res = digits[i] - 5
                    roman.append(maps[500]+(res*maps[100]))
                elif val > 100:
                    res = digits[i] - 0
                    roman.append(res*maps[100])
                elif val > 50:
                    res = digits[i] - 5
                    roman.append(maps[50]*res*maps[10])
                elif val>10:
                    res = digits[i] - 0
                    roman.append(res*maps[10])
                elif val>5:
                    res = digits[i] - 5
                    roman.append(maps[5]+(res*maps[1]))
                else:
                    res = digits[i] - 0
                    roman.append(res*maps[1])
            n-=1
        print("digits:",roman)
        return "".join(roman)

        
