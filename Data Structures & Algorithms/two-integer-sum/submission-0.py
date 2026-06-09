class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(0, len(nums)):
            t = m.get(nums[i])
            if t is None:
                m[target - nums[i]] = i
            else:
                return [t, i]