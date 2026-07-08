class Solution:
    def climbStairs(self, n: int) -> int:
        right = 1
        left = 1
        for _ in range(n-1):
            temp = left 
            left = right + left
            right = temp
        return left 
