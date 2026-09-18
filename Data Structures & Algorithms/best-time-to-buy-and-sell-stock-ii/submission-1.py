class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = l = r = 0

        while r < len(prices):

            if r == l:
                r += 1
                continue
            
            s = prices[r] - prices[l] 

            if s > 0:
                total += s
            
            l += 1
            r += 1
        
        return total


        