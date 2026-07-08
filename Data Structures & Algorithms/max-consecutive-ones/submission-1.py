class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        list_of_ones = []
        one = 0
        for i in range(len(nums)):
            if nums[i]==1:
                one +=1
            elif nums[i]!=1:
                list_of_ones.append(one)
                one = 0
        list_of_ones.append(one)
        return max(list_of_ones)
