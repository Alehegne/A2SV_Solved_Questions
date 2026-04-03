class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def trips(t):
            return sum(t // bus_time for bus_time in time)
        left, right = 1, max(time) * totalTrips # maximum time if all trips are done by the slowest bus
        while left < right:
            mid = left + (right - left) // 2
            if trips(mid) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left
        