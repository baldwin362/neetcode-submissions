from math import sqrt 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for p in points:
            x = p[0]
            y = p[1]
            dist = x**2 + y**2
            max_heap.append([-dist,x,y])
        heapq.heapify(max_heap) # O(n) time complexity 
        while len(max_heap) > k: 
            heapq.heappop(max_heap)
        res = [[x[1],x[2]] for x in max_heap]
        return res
