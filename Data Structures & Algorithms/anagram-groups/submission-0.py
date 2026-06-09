class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        counters = []

        for s in strs:
            c = Counter(s)

            if c not in counters:
                m[len(counters)] = [s]
                counters.append(c)
            else:
                i = counters.index(c)
                m[i].append(s)
        
        return list(m.values())