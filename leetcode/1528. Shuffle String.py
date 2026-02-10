class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        ans = [""]*len(indices)
        for idx,char in zip(indices,s):
            ans[idx] = char
        return "".join(ans)
        
