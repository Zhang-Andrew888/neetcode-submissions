class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for v in tokens:
            try:
                num_stack.append(int(v))
            except ValueError:
                v1 = num_stack.pop()
                v2 = num_stack.pop()

                if "+" == v:
                    num_stack.append(v1 + v2)
                elif "-" == v:
                    num_stack.append(v2 - v1)
                elif "*" == v:
                    num_stack.append(v1 * v2)
                else:
                    num_stack.append(int(v2 / v1))
        
        return num_stack.pop()
                

                    

        
        


