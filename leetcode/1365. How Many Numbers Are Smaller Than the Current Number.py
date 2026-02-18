class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # ans = []
        # for i in range(len(nums)):
        #     c = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             c += 1
        #     ans.append(c)
        # return ans
        sorted_ = sorted(nums)
        hash_ = {}
        for i,num in enumerate(sorted_):
            if num not in hash_:
                hash_[num] = i

        return [hash_[num] for num in nums]


        
