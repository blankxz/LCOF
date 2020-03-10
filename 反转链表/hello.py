# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import copy
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur_node = None
        pre_node = copy.deepcopy(head)
        while pre_node:
            temp = pre_node.next
            pre_node.next = cur_node
            cur_node = pre_node
            pre_node =temp
        return head
    
    
    
s = Solution()
head = ListNode(1)
a = head
for i in range(2,6):
    head.next = ListNode(i)
    head = head.next
    
# while a:
#     print(a.val)
#     a = a.next
c = s.reverseList(a)

while c:
    print(c.val)
    c = c.next