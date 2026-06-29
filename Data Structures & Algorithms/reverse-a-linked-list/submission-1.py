# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList_aux(self, curr, prev):
        if curr is None:
            return prev
        
        nxt = curr.next
        curr.next = prev
        return self.reverseList_aux(nxt, curr)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        return self.reverseList_aux(head, None)
        