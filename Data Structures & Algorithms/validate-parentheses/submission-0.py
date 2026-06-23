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
                
                if stack:
                    m = stack.pop() 
                    if m != v: 
                        return False
                else:
                    return False
            
            else:
                stack.append(ch)
        
        if len(stack) > 0:
            return False

        return True