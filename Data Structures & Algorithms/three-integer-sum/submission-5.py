class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0

        while i < len(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            
            val_i = nums[i]
            target = -1 * nums[i]
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    res.append([val_i, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                
                elif s < target:
                    left += 1
                else:
                    right -= 1

            i += 1

        return res
