class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = Counter(nums)
        for k in f.most_common():
            return k[0]

