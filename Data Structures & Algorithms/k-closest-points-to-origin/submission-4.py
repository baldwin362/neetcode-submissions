from math import sqrt 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(len(points)):
            distance = - sqrt(points[i][0]**2 + points[i][1]**2)
            max_heap.append((distance, points[i]))
        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        res = []
        for i in range(len(max_heap)):
            res.append(max_heap[i][1])
        return res 