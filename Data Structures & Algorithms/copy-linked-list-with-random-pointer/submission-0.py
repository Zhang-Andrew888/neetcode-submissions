"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_curr = new_head = Node(head.val)
        curr = head

        map_m = {head : new_head}

        while curr.next:
            curr = curr.next
            new_curr.next = Node(curr.val)
            new_curr = new_curr.next

            map_m[curr] = new_curr
        
        # reset curr
        curr = head
        
        while curr:
            copy_curr = map_m[curr]

            if curr.random:
                copy_random = map_m[curr.random]
                copy_curr.random = copy_random
            
            curr = curr.next

        return new_head


        
        