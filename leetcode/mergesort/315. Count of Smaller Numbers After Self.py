class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        n = len(nums)

        ans = [0] * n
        def merge(left_half,right_half) -> List[int]:
            # write your code here
            i,j = 0,0
            res = []
            while i < len(left_half) and j < len(right_half):
                if left_half[i][0] <= right_half[j][0]:
                    ans[left_half[i][1]] += j
                    res.append(left_half[i])
                    i += 1
                else:
                    res.append(right_half[j])
                    j += 1
            for k in range(i,len(left_half)):
                ans[left_half[k][1]] += j
                res.append(left_half[k])
            # res.extend(left_half[i:])
            res.extend(right_half[j:])
            return res


        def merge_sort(l,r,arr):
            if l == r:
                return [arr[r]]
            
            mid = (l + r)//2
            left = merge_sort(l,mid,arr)
            right = merge_sort(mid+1,r,arr)

            return merge(left,right)
        for i in range(len(nums)):
            nums[i] = (nums[i],i)
        merge_sort(0,len(nums)-1,nums)
        return ans
