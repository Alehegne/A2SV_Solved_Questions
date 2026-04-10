class Solution:
    def minimumDistance(self, nums: List[int]) -> int:


        dist = defaultdict(list)

        for i,x in enumerate(nums):
            dist[x].append(i)
        
        mn = float('inf')

        for key, arr in dist.items():
            if len(arr) > 2:
                for j in range(len(arr)-2):
                    mn = min(mn,abs(arr[j]-arr[j+1]) + abs(arr[j+1]-arr[j+2]) + abs(arr[j] - arr[j+2]))
        return mn if mn != float('inf') else -1
        