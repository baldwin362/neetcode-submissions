class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        total = 0
        length = float("inf")
        L = 0 #left pointer 
        #R for right pointer 
        for R in range(len(nums)): 
            total += nums[R]
            while total >= target:
                length = min(length, R-L+1)
                total -= nums[L]                    
                L+=1
        return length if length!=float("inf") else 0