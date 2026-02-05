from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        smallest = min(strs,key=len)

        for i,c in enumerate(smallest):
            #iterate over the rest
            for j in range(len(strs)):
                if strs[j][i] != c:
                    return smallest[:i]