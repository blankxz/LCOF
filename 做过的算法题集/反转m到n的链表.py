class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def reverseMN(self,head,m,n):
        extra = LinkNode(-1)
        extra.next = head
        pre = extra
        for i in range(m):
            pre = pre.next
        node = pre
        cur = pre.next
        for i in range(n-m+1):
            tmp = cur.next
            cur.next = node
            node = cur
            cur = tmp
        pre.next.next = cur
        pre.next = node
        return extra.next


testList = [1,2,3,4,5]
head_ = LinkNode(testList[0])
h = head_
for i in range(1,len(testList)):
    head_.next = LinkNode(testList[i])
    head_ = head_.next
# while h:
#     print(h.val)
#     h= h.next

s = Solution()
res = s.deleteNoNNode(h,2,4)
while res:
    print(res.val)
    res= res.next