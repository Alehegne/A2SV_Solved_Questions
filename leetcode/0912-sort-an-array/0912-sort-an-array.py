class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_half,right_half) -> List[int]:
                # write your code here
                i,j = 0,0
                res = []
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        res.append(left_half[i])
                        i += 1
                    else:
                        res.append(right_half[j])
                        j += 1
                res.extend(left_half[i:])
                res.extend(right_half[j:])
                return res



        def merge_sort(l,r,arr):
            if l == r:
                return [arr[r]]
            
            mid = (l + r)//2
            left = merge_sort(l,mid,arr)
            right = merge_sort(mid+1,r,arr)

            return merge(left,right)
        return merge_sort(0,len(nums)-1,nums)
        