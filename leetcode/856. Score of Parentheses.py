class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        for c in s:
            if c == ")":
                sum_ = 0
                while stack[-1] != "(":
                    sum_ += int(stack.pop())
                stack.pop() #removes (
                if sum_ == 0:
                    stack.append(1)
                else:
                    stack.append(sum_ * 2)
            else:
                stack.append(c)
        return sum(stack)
        

        
