from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for val in count.values():
            maxHeap.append(-val)
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1
                if freq != 0:
                    queue.append((freq, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time

