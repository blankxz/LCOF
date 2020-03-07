# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        h = head
        if head.val == val: return head.next
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                return h
            head = head.next
        return h