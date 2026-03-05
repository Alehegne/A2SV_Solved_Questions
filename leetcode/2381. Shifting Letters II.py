class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        shift=[0]*len(s)

        for i in range(len(shifts)):
            l=shifts[i][0]
            r=shifts[i][1]
            if shifts[i][2]==0:
                shift[l]-=1
                if r<len(s)-1:
                    shift[r+1]+=1
            else:
                shift[l]+=1
                if r<len(s)-1:
                    shift[r+1]-=1
                
        #find prefix sum
        for i in range(1,len(shift)):
            shift[i]+=shift[i-1]

        #shift each character
        char_list = list(s)
        for i in range(len(s)):
            cur_char=ord(s[i])-ord('a')
            cur_char=(cur_char+shift[i])%26
            char_list[i]=chr(cur_char+97)
        return "".join(char_list)




        
