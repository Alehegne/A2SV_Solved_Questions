from collections import Counter
from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        freq = Counter() #freq of list1, with value->index
        for i,l in enumerate(list1):
            freq[l] = i
        
        # val_sum = {}
        ans = []
        best=inf
        for i, e in enumerate(list2):
            if e in freq:
                idx_sum = i+freq[e]
                if idx_sum < best:
                    best = idx_sum
                    ans = []
                if idx_sum==best:
                    ans.append(e)
                
        #get min from valus
        # min_ = min(list(val_sum.values()))
        #extract out all with min_
        # ans = []
        # for val, sum in val_sum.items():
        #     if sum == min_:
        #         ans.append(val)
        return ans
        