class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_ = 0

        while num_set:
            # pick any element from the set
            current = num_set.pop()
            cnt = 1

            left = current - 1
            while left in num_set:
                num_set.remove(left)
                cnt += 1
                left -= 1

            right = current + 1
            while right in num_set:
                num_set.remove(right)
                cnt += 1
                right += 1

            max_ = max(max_, cnt)

        return max_
