class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = []

        for s in strs:
            new_str.append(str(len(s)))
            new_str.append("#")
            new_str.append(s)

        return ''.join(new_str)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while len(s) > i:
            length = int(s[i])

            while s[i+1] != '#':
                length = (length * 10) + int(s[i+1])
                i += 1
            i += 1
            strs.append(s[i + 1: length + i + 1])
            i += length + 1

        return strs
        


