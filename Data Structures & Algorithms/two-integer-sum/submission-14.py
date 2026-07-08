class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we want nums[i] + nums[j] == target but we need to rearrange 
        # instead we rearrange to nums[j] == target - nums [i]
        hash = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i