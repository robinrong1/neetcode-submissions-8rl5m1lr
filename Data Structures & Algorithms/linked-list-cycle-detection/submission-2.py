# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast= head 
        slow = head
        
        while slow.next and fast.next.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False