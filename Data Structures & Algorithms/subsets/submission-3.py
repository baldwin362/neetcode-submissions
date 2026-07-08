class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i:int, subset: List[int])->None:    
            if i >= len(nums):
                res.append(subset.copy())
                return 
            #Case n°1: we choose  to include nums[i] inside the subset 
            subset.append(nums[i])
            dfs(i+1, subset)
            #Case n°2: we choose not to include nums[i] inside the subset 
            subset.pop()
            dfs(i+1,subset)
        i = 0
        dfs(i,subset)
        return res 