# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return

        size = 1
        curr = head
        while curr.next:
            size += 1
            curr = curr.next
        
        if size - n <= 0:
            head = head.next
            return head
        
        i = size - n
        curr = head
        for _ in range(i - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        
        return head