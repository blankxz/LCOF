class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        a = head
        ind = 0
        while head.next:
            ind += 1
            if ind >= k:
                a = a.next
            head = head.next
        return a


a = ListNode(1)
b = a
for i in range(2,6):
    a.next = ListNode(i)
    a = a.next

s = Solution()
a = s.getKthFromEnd(b,3)

print(a.val)