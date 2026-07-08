class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap) #conversion of stones in a max-heap allowing O(1) retrieval of maximum value 
        #creating a heap has a O(nlog(n)) time complexity
        while len(max_heap) > 1:
            y = - heapq.heappop(max_heap) # O(1) time complexity
            x = - heapq.heappop(max_heap)
            if x!=y:
                heapq.heappush(max_heap, - (y-x))
            if len(max_heap) == 0:
                return 0
        return -1* max_heap[0]
