class Solution:
    def combinationSum_aux(self, prelist, nums, start, target) -> List[List[int]]:
        if target == 0:
            return [prelist]   
        if target < 0:
            return []

        result = []
        for i in range(start, len(nums)):
            result.extend(self.combinationSum_aux(prelist + [nums[i]], nums, i, target - nums[i]))
        return result

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.combinationSum_aux([], nums, 0, target)