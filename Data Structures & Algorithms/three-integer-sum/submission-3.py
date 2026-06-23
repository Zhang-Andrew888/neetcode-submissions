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
            m = {}

            j = i + 1

            while j < len(nums):
                val_j = nums[j]

                if val_j in m:
                    res.append([val_i, m[val_j], val_j])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j+= 1
                else:
                    m[target - val_j] = val_j
                    j += 1

                
            i += 1
        

        return res
