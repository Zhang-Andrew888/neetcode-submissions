class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
    
        s = set(nums)
        seq = 1

        for num in s:
            if (num -1) not in s:
                curr_seq = 1

                while num + curr_seq in s:
                    curr_seq += 1
            
                if curr_seq > seq:
                    seq = curr_seq
        
        return seq

 
