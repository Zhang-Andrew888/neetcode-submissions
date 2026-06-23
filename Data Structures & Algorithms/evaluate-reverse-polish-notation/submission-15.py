class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for v in tokens:
            if "+" == v:
                v1 = num_stack.pop()
                v2 = num_stack.pop()
                num_stack.append(v1 + v2)
            elif "-" == v:
                v1 = num_stack.pop()
                v2 = num_stack.pop()
                num_stack.append(v2 - v1)
            elif "*" == v:
                v1 = num_stack.pop()
                v2 = num_stack.pop()
                num_stack.append(v1 * v2)
            elif "/" == v:
                v1 = num_stack.pop()
                v2 = num_stack.pop()
                num_stack.append(int(v2 / v1))
            else:
                num_stack.append(int(v))
        
        return num_stack.pop()
                

                    

        
        


