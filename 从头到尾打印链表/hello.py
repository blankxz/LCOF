class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        return lis[::-1] #考试安排的好多
