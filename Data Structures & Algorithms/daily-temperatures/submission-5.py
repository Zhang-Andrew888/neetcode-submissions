class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                prev_i = stack.pop()[0]
                res[prev_i] = i - prev_i
            
            stack.append((i, v))


        return res