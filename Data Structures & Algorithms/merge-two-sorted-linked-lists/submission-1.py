# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list2.val < list1.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        
        current = head
        while list1 and list2:
            if list2.val < list1.val:
                current.next = list2
                current = current.next
                list2 = list2.next
            else:
                current.next = list1
                current = current.next
                list1 = list1.next
        if not list1:
            current.next = list2
        if not list2:
            current.next = list1
        return head
