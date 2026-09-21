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
        mapping = {None: None}
        current = head
        while current:
            copy = Node(current.val)
            mapping[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = mapping[current]
            copy.next = mapping[current.next]
            copy.random = mapping[current.random]
            current = current.next
        
        return mapping[head]
