class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        current_streak_of_ones = 0
        max_streak_of_ones = 0
        for i in range(len(nums)): 
            if nums[i]==0:
                if current_streak_of_ones > max_streak_of_ones:
                    max_streak_of_ones = current_streak_of_ones 
                current_streak_of_ones = 0
            if nums[i]==1:
                current_streak_of_ones+=1
        if current_streak_of_ones > max_streak_of_ones: 
            max_streak_of_ones = current_streak_of_ones
        return max_streak_of_ones