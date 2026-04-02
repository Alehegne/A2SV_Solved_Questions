class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        def check(p):
            st = []

            for c in p:
                if c == "(":
                    st.append(c)
                else:
                    if not st:
                        return False
                    st.pop()
            return True if not st else False

        
        ans = []

        def back(path,op,close):
            if op == close == 0:
                res = ''.join(path)
                if check(res):
                    ans.append(res)
                return
            
            if op:
                path.append("(")
                back(path,op-1,close)
                path.pop()
            if close:
                path.append(")")
                back(path,op,close-1)
                path.pop()
            

        back([],n,n)
        return ans



        