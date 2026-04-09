class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        ans = 0

        def merge(left,right):
            nonlocal ans

            ptr = 0
            for i in range(len(left)):
                while ptr < len(right) and left[i] > 2 * right[ptr]:
                    ptr += 1
                ans += ptr

            i = j = 0
            temp = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    temp.append(left[i])
                    i += 1
                else:
                    temp.append(right[j])
                    j += 1
            temp.extend(right[j:])
            temp.extend(left[i:])
           

            return temp
        def merge_s(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr)//2

            left = merge_s(arr[:mid])
            right = merge_s(arr[mid:])
            return merge(left,right)
        merge_s(nums)
        return ans
        