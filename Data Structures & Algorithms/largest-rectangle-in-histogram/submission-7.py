class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                area = (i - idx) * h
                if area > max_area:
                    max_area = area
                start = idx

            stack.append((start, height))
        
        for pair in stack:
            area = (len(heights) - pair[0]) * pair[1]

            if area > max_area:
                max_area = area
        
        return max_area

