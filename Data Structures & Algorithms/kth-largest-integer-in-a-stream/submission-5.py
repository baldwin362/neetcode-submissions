class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k  = nums, k 
        heapq.heapify(self.minheap) #convert the list into a heap data structure 
        while len(self.minheap) > k:
            heapq.heappop(self.minheap) #pops the smallest element in the heap
        # [4,5,7,2]
        # 2 
        # --> 4 (left child)
        # --> 5 (right child)
        # --> 7 (5's left child)
        #min value --> 2 heap.heappop(your_heap) -> pop 2
    def add(self, val:int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]