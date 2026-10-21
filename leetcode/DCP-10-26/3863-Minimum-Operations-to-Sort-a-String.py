class Solution:
    def minOperations(self, s: str) -> int:
        

        # smallest,largest = 'z','a'

        # for c in s:
        #     if c > largest:
        #         largest = c
        #     if c < smallest:
        #         smallest = c
        
        ss = sorted(s)

        cnt = 1
        for i in range(1,len(ss)):
            if ss[i] == ss[i-1]:
                cnt += 1
            else:
                break
        cnte = 1
        for i in range(len(ss)-2,-1,-1):
            if ss[i] == ss[i+1]:
                cnte += 1
            else:
                break
        

        if ''.join(ss) == s:
            return 0
        if len(s) < 3:
            return -1
        ans = 0
        if ss[0] != s[0]:
            ans += 1
        if ss[-1] != s[-1]:
            ans += 1
        if cnt == 1 and ss[0] == s[-1] and cnte == 1:
            ans += 1
        print(ss)
        return max(ans,1)
