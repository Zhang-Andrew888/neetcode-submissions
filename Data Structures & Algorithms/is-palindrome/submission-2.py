class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            l = s[left].lower()
            r = s[right].lower()

            if not l.isalnum():
                left += 1
            elif not r.isalnum():
                right -= 1
            else:
                if l != r:
                    return False
                
                left += 1
                right -= 1
        
        return True