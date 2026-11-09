import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(maxheap, (distance, [x, y]))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        result = []
        while maxheap:
            coordinate = heapq.heappop(maxheap)
            result.append(coordinate[1])
        return result
            