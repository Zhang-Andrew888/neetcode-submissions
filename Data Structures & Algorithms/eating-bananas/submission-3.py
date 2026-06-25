class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            total_time = 0
            for b in piles:
                total_time += math.ceil(b / m)

            if total_time > h:
                l = m + 1
            else:
                r = m - 1
        
        return l

