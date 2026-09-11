class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # create recursive function that intakes nums, index of list and returns a list of all subsets for that range
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

