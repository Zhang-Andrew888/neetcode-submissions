class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        
        for i in range(1, len(nums)):
            pre.append(nums[i -1] * pre[i-1])
            suf.append(nums[len(nums) -i] * suf[i -1])
        res = []
        for j in range(len(nums)):
            res.append(pre[j] * suf[len(nums) - j -1])
        return res