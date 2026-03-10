class Solution:
    def decodeString(self, s: str) -> str:

        stack = [] #keeps track of all chars except "]"

        for i,char in enumerate(s):

            if char == "]":
                res = ""
                while stack[-1] != "[":
                    res = stack[-1] + res
                    stack.pop()
                stack.pop()#removes "["
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack[-1] + num
                    stack.pop()
                stack.append(res*int(num))
            else:
                stack.append(char)
        return "".join(stack)
        
