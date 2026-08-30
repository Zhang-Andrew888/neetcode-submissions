# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal and then start incrementing from there
        # peform k - 1
        # exit loop as soon as the number of seen elements is equal to k and therefore we have found it
        stack = []
        current = root
        seen = 0

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            seen += 1

            if seen == k:
                return current.val
            
            current = current.right
        
        return -1


