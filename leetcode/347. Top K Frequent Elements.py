class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        f = Counter(nums)

        s = sorted(f,key=lambda x: -f[x])
        return s[:k]
        
