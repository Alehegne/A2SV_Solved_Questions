class Solution:
    def hIndex(self, citations: List[int]) -> int:
        

        n = len(citations)
        citations.sort()
        h = 0
        j = 0

        for i in range(n,0,-1):
            if citations[j] >= i:
                return i
            j += 1
        return 0
