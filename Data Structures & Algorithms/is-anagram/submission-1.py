class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        m = {}
        for ch in s:
            m[ch] = m.get(ch, 0) + 1
        
        for ch in t:
            if m.get(ch) is None:
                return False
            
            m[ch] -= 1
            if m[ch] == 0:
                del m[ch]
        
        return not m