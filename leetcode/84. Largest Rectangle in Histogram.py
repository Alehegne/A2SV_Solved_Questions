class Solution:
    def _next_smaller(self,arr):
        next_ = defaultdict(lambda:-1)

        st = []#increasing
        for i,num in enumerate(arr):
            
            while st and num < arr[st[-1]]:
                top = st.pop()
                next_[top] = i
            st.append(i)
        return [next_[i] for i in range(len(arr))]
    def _previous_smaller(self,arr):
        previous = defaultdict(lambda:-1)
        st = []#increasing
        n = len(arr)
        for i in range(n-1,-1,-1):
            
            while st and arr[i] < arr[st[-1]]:
                top = st.pop()
                previous[top] = i
            st.append(i)


        return [previous[i] for i in range(n)]
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_ = 0
        n = len(heights)
        previous_smaller = self._previous_smaller(heights)
        next_smaller = self._next_smaller(heights)

        for i,num in enumerate(heights):
            # left,right = i,i
            # #next smaller
            # while right + 1 < n and heights[right+1] >= num:
            #     right += 1
            # #previous smaller
            # while left - 1 > 0 and heights[left-1] >= num:
            #     left -= 1
            left = 0 if previous_smaller[i] == -1 else previous_smaller[i] + 1
            right = n-1 if next_smaller[i] == -1 else next_smaller[i] - 1
            max_ = max((right-left+1)*num,max_)
        return max_
            
