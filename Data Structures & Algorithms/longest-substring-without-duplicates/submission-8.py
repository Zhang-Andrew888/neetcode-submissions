class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start at initial index
        # keep increasing r as long as l not equal to r
        # array of 26 storing booleans. If boolean false, make it true and continue
        # if true, then increment l also. 
        # always increment r

        l = 0
        res = 0
        mp = {}

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            
            mp[s[r]] = r
            res = max(res, r - l + 1)
        
        return res

        