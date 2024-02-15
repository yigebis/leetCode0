class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        shots = 1
        points.sort(key=lambda x: x[1])
        pre_last = points[0][1]
        # print(points)
        for i in range(1, len(points)):
            if points[i][0] > pre_last:
                shots += 1
                pre_last = points[i][1]
        
        return shots

