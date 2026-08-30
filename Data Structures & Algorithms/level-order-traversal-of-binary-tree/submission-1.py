# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Peform BFS where you store hashmap that stores the depth at which the list is
        # Create a list where each time you get a new value, refer to the hasmap for the depth and then add it respectively to its sublist. 
        # always append operation will add it in order by invariant of BT and how we are searching BFS
        # return mega list!
        li = []

        depth = {}
        q = deque()

        if root is None:
            return []
        
        depth[None] = 0
        q.append((root, None))

        while q:
            c, p = q.popleft()

            i = depth[p]

            if len(li) <= i:
                li.append([c.val])
            else:
                sublist = li[i]
                sublist.append(c.val)
            
            depth[c] = depth[p] + 1
            
            if c.left:
                q.append((c.left, c))
            if c.right:
                q.append((c.right, c))
        
        return li

            

    
        

