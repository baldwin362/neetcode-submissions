class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algorithm running on O(n)
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            curSum = max(0,curSum) #curSum's positive part to ensure we don't have a negative sum 
            curSum += n
            maxSum = max(curSum, maxSum)
        return maxSum 