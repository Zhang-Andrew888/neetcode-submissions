class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start at initial index
        # keep increasing r as long as l not equal to r
        # array of 26 storing booleans. If boolean false, make it true and continue
        # if true, then increment l also. 
        # always increment r

        r = seq = m_seq = 0
        q = deque()
        seen = set()

        while r < len(s):
            while s[r] in seen:
                c = q.popleft()
                seen.remove(c)
                seq -= 1

            q.append(s[r])
            seen.add(s[r])
            seq += 1

            r += 1

            if m_seq < seq:
                m_seq = seq
        
        return m_seq

        