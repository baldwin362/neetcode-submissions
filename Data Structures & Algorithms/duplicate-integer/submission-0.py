class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for el in nums:
            if el not in hash:
                hash[el] = 1
            else:
                return True 
        return False 
