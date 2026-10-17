class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def sm(x):
            s = 0
            for v in str(x):
                s += int(v)
            return s



        sorted_ = sorted(nums,key = lambda x:(sm(x),x))

        # print(sorted_)
        idxs = {}
        for i in range(len(sorted_)):
            idxs[sorted_[i]] = i

        ans = 0
        # 5:3
        # print(idxs)
        for i in range(len(nums)):
            pos = idxs[nums[i]]
            while pos != i:
                ans += 1
                nums[pos],nums[i] = nums[i],nums[pos]
                pos = idxs[nums[i]]  
        return ans
        

"""
22,14,33,7 => 4,5,6,7 => no swaps
18,43,34,16 => 9,7,7,7 => 
16 43 34 18 => 7 7 7 9
16 34 43 18 => 7 7 7 9

4 3 2 1 => 2 way


1 2 3 4

2 4 1 3 => 
4 2 1 3
3 2 1 4
1 2 3 4

37,100
100 37

18 43 34 16 => 16 34 43 18
16 43 34 18
16 34 43 18


37 100 => 100 37 => 100:0,37:1
"""

