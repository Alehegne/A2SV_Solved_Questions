class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dp(left,right):


            if left == right:
                return 1
            if left > right:
                return 0
            

            if s[left] == s[right]:
                return 2 + dp(left + 1,right - 1)
            return max(dp(left,right-1),dp(left+1,right))
        return dp(0,len(s)-1)