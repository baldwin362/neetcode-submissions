class Solution:
    def climbStairs(self, n: int) -> int:
        #basically if we call F(n) the function that returns the numbers of ways 
        # to climb n stairs 
        # F(n) = F(n-1) + F(n-2)
        # because we either come from stair n-1 or stair n-2
        # this is the fibonacci sequence 
        ways = [0,1]
        i = 0
        while i<n:
            temp = ways[1]
            ways[1] = ways[1] + ways[0]
            ways[0] = temp
            i+=1
        return ways[1] 