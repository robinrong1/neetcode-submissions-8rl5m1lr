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
        curr = head
        hashMap = {}
        while curr:
            clone = Node(curr.val, None, None)
            hashMap[curr] = clone
            curr = curr.next
        for og_node, clone_node in hashMap.items():
            clone_node.random = hashMap.get(og_node.random, None)
            clone_node.next = hashMap.get(og_node.next, None)
        return hashMap[head]