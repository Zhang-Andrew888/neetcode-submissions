class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for ch in s:
            if ch in mappings:
                v = mappings[ch]
                
                if stack and stack[-1] == v:
                    m = stack.pop() 
                else:
                    return False
            
            else:
                stack.append(ch)
        
        if len(stack) > 0:
            return False

        return True