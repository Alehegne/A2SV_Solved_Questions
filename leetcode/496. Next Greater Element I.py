class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = [] #monotonically decreasing
        n = len(nums2)
        next_ = defaultdict(lambda:-1)

        for i in range(n):

            while stack and nums2[i] > stack[-1]:
                next_[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        return [next_[num] for num in nums1]


        
        
