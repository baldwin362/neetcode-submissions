class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-el for el in nums]
        heapq.heapify(max_heap)
        cur = 0
        while k > 0:
            cur = heapq.heappop(max_heap)
            k-=1
        return -cur