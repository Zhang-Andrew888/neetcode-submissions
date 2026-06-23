class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_comb_list = sorted(zip(position, speed), key = lambda x: x[0])
        stack = []

        for pair in sorted_comb_list:
            if stack:
                prev_time = (target - stack[-1][0]) / stack[-1][1]
                curr_time = (target - pair[0]) / pair[1]

                while prev_time <= curr_time:
                    stack.pop()

                    if not stack:
                        break

                    prev_time = (target - stack[-1][0]) / stack[-1][1]
                
            stack.append(pair)
        
        return len(stack)
        

