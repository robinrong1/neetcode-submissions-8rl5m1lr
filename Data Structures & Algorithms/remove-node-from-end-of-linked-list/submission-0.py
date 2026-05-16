# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get to the end of the list
        # go backwards by n
        dummy = ListNode(0, head)

        end = head
        count = 1
        while end.next:
            end = end.next
            count += 1
        
        #count is length
        count -= n
        #count is length - n
        curr = dummy
        for i in range(count):
            curr = curr.next
        #now dummy.next is the node to be removed

        curr.next = curr.next.next
        return dummy.next