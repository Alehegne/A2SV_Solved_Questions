from typing import List
from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)

        i=0
        while i in freq:
            i+=1
        return i

        