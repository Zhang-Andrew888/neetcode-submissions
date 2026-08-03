# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy_head = ListNode()
        carry_over = 0

        while l1 or l2:
            if not l1:
                num = l2.val + carry_over

                if num >= 10:
                    carry_over = 1
                else:
                    carry_over = 0
    
                curr.next = ListNode(num % 10)
                l2 = l2.next
            elif not l2:
                num = l1.val + carry_over

                if num >= 10:
                    carry_over = 1
                else:
                    carry_over = 0

                curr.next = ListNode(num % 10)
                l1 = l1.next
            else:
                num = l1.val + l2.val + carry_over
    
                if num >= 10:
                    carry_over = 1
                else:
                    carry_over = 0
                
                curr.next = ListNode(num % 10)

                l1 = l1.next
                l2 = l2.next
            
            curr = curr.next
        
        if carry_over > 0:
            curr.next = ListNode(1)
        
        return dummy_head.next
            
        