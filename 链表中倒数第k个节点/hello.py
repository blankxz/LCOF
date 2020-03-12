class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        while head:
            print(head.val)
            head = head.next
        return head


a = ListNode(1)
b = a
for i in range(2,6):
    a.next = ListNode(i)
    print(a.val)
    a = a.next

s = Solution()
a = s.getKthFromEnd(b,3)

print(a)