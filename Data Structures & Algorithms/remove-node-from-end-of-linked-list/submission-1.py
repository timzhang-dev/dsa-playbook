# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = head
        count = 0
        while current:
            current = current.next
            count += 1
        
        current = dummy
        count_2 = 0
        while current:
            if count_2 == count - n:
                current.next = current.next.next
            current = current.next
            count_2 += 1
        return dummy.next