# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
    
        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head

        while list1 is not None or list2 is not None:
            if list1 is None:
                curr.next = list2
                break
            
            if list2 is None:
                curr.next = list1
                break

            node = None

            if list1.val > list2.val:
                node = list2
                list2 = list2.next
            else:
                node = list1
                list1 = list1.next
            
            curr.next = node
            curr = curr.next

        return head

        