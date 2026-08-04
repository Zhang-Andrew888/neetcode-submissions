class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)

        for n in nums:
            if seen[n] > 0:
                return n

            seen[n] = 1

        return -1 
        