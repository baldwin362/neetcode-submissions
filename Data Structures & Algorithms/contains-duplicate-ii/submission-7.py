class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:
            return False
        window = set() #sorted hash 
        # O(n) time complexity --> naive method 
        # going through every single element and constantly checking for a further duplicate 
        # without memorizing --> O(n*k) time complexity
        #Memorize the values that we've had in the previous window checking 
        # --> O(n)
        L = 0
        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False 

