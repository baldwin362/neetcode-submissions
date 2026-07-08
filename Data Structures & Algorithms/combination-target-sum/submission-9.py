class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i:int, subset: List[int], total: int )-> None:
            if total == target:
                res.append(subset.copy())
                return 
            if i>=len(nums) or total > target:
                return 
 
            #Case n°1: we choose to take nums[i]
            subset.append(nums[i])
            dfs(i, subset, total+nums[i])

            #Case n°2: we choose to not take nums[i]
            subset.pop()
            dfs(i+1,subset, total)


        i = 0
        total = 0
        dfs(i,subset, total)
        return res 