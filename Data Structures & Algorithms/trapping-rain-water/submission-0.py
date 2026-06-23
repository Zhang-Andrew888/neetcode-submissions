class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
    
        l, r = 1, len(height) - 2
        max_l, max_r = height[0], height[len(height) - 1] 
        res = 0

        while l <= r:
            if max_l <= max_r:
                if height[l] < max_l:
                    res += max_l - height[l]
                else:
                    max_l = height[l]
                l += 1
            else:
                if height[r] < max_r:
                    res += max_r - height[r]
                else:
                    max_r = height[r]
                
                r-= 1
        
        return res
                
                


            
            
