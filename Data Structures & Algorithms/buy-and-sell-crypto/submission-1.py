class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers. If the value increases keep, if decreases pop and keep as max number so far. Compare as we go on

        max_value = -1
        l = r = 0

        while r < len(prices):
            i = prices[r] - prices[l]

            if i > max_value:
                max_value = i
            else:
                if prices[l] > prices[r]:
                    l = r
                
            r += 1
            
        return max_value
                
            
        