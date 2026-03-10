class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        next_ = defaultdict(lambda:0)
        stack = []#monotonically decreasing
        n = len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                next_[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return [next_[i] for i in range(n)]



        
