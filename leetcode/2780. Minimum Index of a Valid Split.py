class Solution:
    def minimumIndex(self, nums: List[int]) -> int:


        f = Counter(nums)
        vis = Counter()
        n = len(nums)

        for i,num in enumerate(nums):

            vis[num] += 1
            f[num] -= 1
            left_l = i + 1
            right_l = n - i- 1
            if f[num] > right_l//2 and vis[num] > left_l//2:
                return i
        return -1

        
