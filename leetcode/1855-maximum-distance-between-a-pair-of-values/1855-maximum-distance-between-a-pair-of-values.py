class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:


        ans = float('-inf')
        for i,num in enumerate(nums1):
            left,right = 0,len(nums2) - 1

            while left <= right:
                mid = (left + right)//2
                if nums2[mid] >= num:
                    left = mid + 1
                else:
                    right = mid - 1
            idx = left - 1
            if idx >= i:
                ans = max(ans,idx - i)
        return ans if ans != float('-inf') else 0
        




        