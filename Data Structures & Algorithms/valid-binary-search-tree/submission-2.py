# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Just peform preorder traversal where we keep track of just one value and see if it is in increasing order
        curr = root
        res = []

        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left

                while prev.right is not None and prev.right != curr:
                    prev = prev.right

                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    res.append(curr.val)
                    curr = curr.right
        
        prev = res[0]
        for i in range(1, len(res)):
            if prev >= res[i]:
                return False

            prev = res[i]
        
        return True





        