class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # n = len(citations)
        # # citations.sort()
        # h = 0
        # j = 0

        # for i in range(n,0,-1):
        #     if citations[j] >= i:
        #         return i
        #     j += 1
        # return 0

        n = len(citations)

        def left_b(curr):
            left = 0
            right = n

            while left < right:
                mid = left + (right - left)//2

                if citations[mid] >= curr:
                    right = mid
                else:
                    left = mid + 1
            return left
        curr = n
        while curr > 0:
            left = left_b(curr)
            if n - left >= curr:
                return curr
            curr -= 1
        return 0