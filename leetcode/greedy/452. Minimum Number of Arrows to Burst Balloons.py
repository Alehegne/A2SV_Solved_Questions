class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()

        arr = [points[0]]
        arrow = 1
        limit = points[0][1] #
        for idx,point in enumerate(points[1:]):
            if point[0] > arr[-1][1] or point[0] > limit:
                arr.append(point)
                limit = point[1]
                arrow += 1
            limit = min(point[1],limit)
        return arrow







        
