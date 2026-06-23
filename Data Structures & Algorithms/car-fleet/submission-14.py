class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_comb_list = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        stack = []

        for pair in sorted_comb_list:
            time = (target - pair[0]) / pair[1]
            stack.append(time)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        

