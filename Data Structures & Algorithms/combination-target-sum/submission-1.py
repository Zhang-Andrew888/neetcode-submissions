class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def dfs(n, pre_list, nums, target):
            final_list = []

            if target == 0:
                return [pre_list]
            
            if target < 0:
                return []
            
            for i in range(n, len(nums)):
                i_list = dfs(i, (pre_list + [nums[i]]), nums, target - nums[i])

                if i_list:
                    final_list.extend(i_list)
            
            return final_list
        
        return dfs(0, [], nums, target)
                