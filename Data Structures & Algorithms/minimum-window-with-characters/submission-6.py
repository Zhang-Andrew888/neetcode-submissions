class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we will use sliding window
        # create a freq table counting all instances in t
        # create window in the substring. start window at first occurence of t
        # if t encounter, decrement freq table respective char. 
        # if t encoutner is same as l AND freq table is 0, shift window
        # return substring between l and r

        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1
        
        l = 0
        while l < len(s) and s[l] not in freq_t:
            l += 1
        
        if l >= len(s):
            return ""
        
        freq_t[s[l]] -= 1
        res = ""
        
        if len(t) == 1 and freq_t[s[l]] == 0:
            return s[l]

        for r in range(l + 1, len(s)):
            if s[r] in freq_t:
                freq_t[s[r]] -= 1
            
            is_valid_substring = True
            for num in freq_t.values():
                if num > 0:
                    is_valid_substring = False
            
            if is_valid_substring:

                # greedily shrink l now
                while s[l] not in freq_t or freq_t[s[l]] < 0:
                    if s[l] in freq_t:
                        freq_t[s[l]] += 1

                    l += 1

                if res == "" or len(res) > r - l + 1:
                    res = s[l:r + 1]
    
        return res