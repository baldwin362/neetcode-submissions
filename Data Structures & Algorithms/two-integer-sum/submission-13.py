class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash ={}
        # nums[i] + nums[j] == target
        # <--> target - nums[i] == nums[j]
        for i,n in enumerate(nums):
            if target - n in hash:
                return [hash[target-n],i]
            else:
                hash[n] = i 
                