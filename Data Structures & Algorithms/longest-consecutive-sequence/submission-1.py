class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
    
        s = set(nums)
        cands = set()

        for num in s:
            if (num -1) not in s:
                cands.add(num)
        
        seq = 1
        for cand in cands:
            curr_seq = 1
            while cand + curr_seq in s:
                curr_seq += 1
            
            if curr_seq > seq:
                seq = curr_seq
        
        return seq

 
