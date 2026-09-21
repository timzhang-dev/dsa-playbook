# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            value = v1 + v2 + carry
            if value >= 10:
                carry = 1
                current.next = ListNode(value % 10)
            else:
                current.next = ListNode(value)
                carry = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next
           
        if carry != 0:
            current.next = ListNode(1)
        
        return dummy.next




