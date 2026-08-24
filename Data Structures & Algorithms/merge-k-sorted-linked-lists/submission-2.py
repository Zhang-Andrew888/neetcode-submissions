# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case is length of list is 0, return list
        # inductive is assuming we can do n lists, how can we do n + 1 lists (pop one of them)
        # i.e [[1], [2,3], [0]] -> [[1], [2,3]] with the running list [0]
        # 
        # map number to LinkedList. Make each mapping a bucket 
        # create another list that stores numbers in ascending order. Keep reinserting as you pop numbers if the number does not exist in the list

        # num to list
        mappings = {}

        for li in lists:
            if li is None:
                pass
            elif li.val not in mappings:
                mappings[li.val] = [li.next]
            else:
                # add to mappings
                mappings[li.val].append(li.next)
        
        sorted_nums = sorted(list(mappings))

        dummy_head = curr = ListNode()

        while sorted_nums:
            num_lists = mappings[sorted_nums[0]]

            for li in num_lists:
                curr.next = ListNode(sorted_nums[0], None)
                curr = curr.next

                if li is None:
                    pass
                elif li.val in mappings:
                    mappings[li.val].append(li.next)
                else:
                    mappings[li.val] = [li.next]
                    sorted_nums.append(li.val)
            
            # invariant is that this will pop sorted_nums[0]
            sorted_nums.pop(0)
            sorted_nums.sort()
        
        return dummy_head.next



           




        