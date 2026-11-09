import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for i in range(len(points)):
            points[i] = (-(math.sqrt((points[i][0])**2 + (points[i][1])**2)), points[i])
        heapq.heapify(points)
        maxheap = points
        while len(maxheap) > k:
            heapq.heappop(points)
        while maxheap:
            coordinate = heapq.heappop(points)
            result.append(coordinate[1])
        return result
            