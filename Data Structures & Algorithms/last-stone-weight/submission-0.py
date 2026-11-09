import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        maxheap = stones

        while maxheap and len(maxheap) >= 2:
            top1 = heapq.heappop(maxheap)
            top2 = heapq.heappop(maxheap)
            if top2 > top1:
                heapq.heappush(maxheap, top1 - top2)
        if maxheap:
            return -maxheap[0]
        else:
            return 0



