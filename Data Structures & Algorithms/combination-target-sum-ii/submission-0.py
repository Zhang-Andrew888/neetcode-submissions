class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res. 
        # first sort candidates into ascending order list
        # perform dfs on it where we are keeping track of nums (potential solutions), target-value (decreasing for each number seen in nums), and i index. 
        # diff = target_value - new_value
        # if diff is negative, return nothing
        # if diff is 0, append numbers to the res list and then return 
        # if diff is positive, append new number found and then iterate through remaining indexes.
        candidates.sort()
        res = []

        def dfs(i, nums, t):
            diff = t - candidates[i]

            if diff < 0:
                return
            
            nums = nums + [candidates[i]]
            
            if diff == 0:
                res.append(nums)
                return
            
            for j in range(i + 1, len(candidates)):
                if j > i + 1 and candidates[j] == candidates[j - 1]:
                    continue

                dfs(j, nums, diff)
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue

            dfs(i, [], target)
        
        return res

        
