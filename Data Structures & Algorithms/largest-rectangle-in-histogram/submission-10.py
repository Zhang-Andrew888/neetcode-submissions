class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                max_area = max((i - idx) * h, max_area)
                start = idx

            stack.append((start, height))
        
        for pair in stack:
            max_area = max((len(heights) - pair[0]) * pair[1], max_area)

        return max_area

