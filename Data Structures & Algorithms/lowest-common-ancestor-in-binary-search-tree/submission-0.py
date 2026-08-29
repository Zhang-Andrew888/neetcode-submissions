# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # peform dfs until we see p and q. We want to record the queue of what we have visited
        # get queue of visited nodes for both p and q. 
        # compare the size of queue and pop greatest value queue. 

        # dictionary: child value to parent node
        visited = {root.val: None}

        # queue of what to visit. BFS style
        queue = deque()
        queue.append(root)

        while p.val not in visited or q.val not in visited:
            n = queue.popleft()

            if n.left:
                queue.append(n.left)
                visited[n.left.val] = n
            
            if n.right:
                queue.append(n.right)
                visited[n.right.val] = n
        
        # grab the parent node of each one as p != q
        p_curr = visited[p.val]
        q_curr = visited[q.val]

        # queue of keeping track of elements added. 
        p_stack = deque()
        q_stack = deque()

        # stack all the way to the base root
        while p_curr:
            p_stack.append(p_curr)
            p_curr = visited[p_curr.val]
        
        while q_curr:
            q_stack.append(q_curr)
            q_curr = visited[q_curr.val]
        
        i = len(p_stack) - len(q_stack)

        if i > 0:
            while i > 0:
                pop = p_stack.popleft()

                if pop.val == q.val:
                    return q

                i -= 1
        elif i < 0:
            i = -i

            while i > 0:
                pop = q_stack.popleft()

                if pop.val == p.val:
                    return p

                i -= 1
        
        while q_stack[0] != p_stack[0]:
            q_stack.popleft()
            p_stack.popleft()
        
        return q_stack[0]

            
            