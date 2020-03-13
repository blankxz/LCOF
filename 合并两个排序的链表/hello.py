class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        a = head
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 or l2:
            if l1 and l2 and l1.val == l2.val:
                head.next = ListNode(l1.val)
                head = head.next
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
                l2 = l2.next
            while l1 and l2 and (l1.val < l2.val):
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            while l1 and l2 and l1.val > l2.val:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
            if l1 == None and l2 != None:
                while l2:
                    head.next = ListNode(l2.val)
                    head = head.next
                    l2 = l2.next
            if l2 == None and l1 != None:
                while l1:
                    head.next = ListNode(l1.val)
                    head = head.next
                    l1 = l1.next
        return a.next
                
        
        
s = Solution()
head1 = ListNode(2)
# head1.next = ListNode(2)
# head1.next.next = ListNode(4)

head2 = ListNode(1)
# head2.next = ListNode(3)
# head2.next.next = ListNode(4)

a = s.mergeTwoLists(head1,head2)

while a:
    print(a.val)
    a = a.next