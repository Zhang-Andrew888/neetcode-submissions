# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # slow, fast approach
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reorder second half of Linked List
        prev_2 = None
        curr_2 = slow
        while curr_2:
            temp = curr_2.next
            curr_2.next = prev_2 

            prev_2 = curr_2      
            curr_2 = temp
    
        # combine prev_2 and head
        curr = head

        while prev_2 and prev_2.next:
            temp = curr.next

            # insert node
            curr.next = prev_2

            # first increment prev_2 and then change second pointer
            prev_2 = prev_2.next
            curr.next.next = temp

            curr = temp
        





        

