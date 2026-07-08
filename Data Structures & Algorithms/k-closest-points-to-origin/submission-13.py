class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)
        for p in points:
            x = p[0]
            y = p[1]
            dist = x**2 + y**2
            heapq.heappush(max_heap, [-dist,x,y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = [[p[1],p[2]] for p in max_heap]
        return res