# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isEqualTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        return root1.val == root2.val and self.isEqualTree(root1.left, root2.left) and self.isEqualTree(root1.right, root2.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # assume that the current root IS the subroot. 
        # if values are equal, go down on left and right until both sides end in null. If that is correct, return true
        # else, if values are not equal, shift isSubTree check onto the left and right two nodes
        if self.isEqualTree(root, subRoot):
            return True
        else:
            if root.left is None and root.right is None:
                 return False
            
            if root.left is None:
                return self.isSubtree(root.right, subRoot)
            
            if root.right is None:
                return self.isSubtree(root.left, subRoot)

            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        