class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for ch in s:
            if m.get(ch) is None:
                m[ch] = 0
            m[ch] += 1
        
        for ch in t:
            if m.get(ch) is None:
                return False
            
            m[ch] -= 1
            if m[ch] == 0:
                del m[ch]
        
        if not m:
            return True
        
        return False