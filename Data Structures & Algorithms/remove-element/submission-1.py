class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        n = len(nums)
        while i<n:
            if nums[i]!=val:
                nums[k], nums[i] = nums[i], nums[k]
                i+=1
                k+=1
            else:
                i+=1
        return k