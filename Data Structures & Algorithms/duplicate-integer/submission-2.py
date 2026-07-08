class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {} #contain all the unique values {value : occurence}

        for n in nums:
            if n not in hash:
                hash[n] = 1
            else:
                return True

        return False 