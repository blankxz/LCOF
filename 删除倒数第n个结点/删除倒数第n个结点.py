class LinkNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def deleteNoNNode(self,head,n):
        h = head
        h1 = head
        h2 = head
        while h1 and h2:
            if n>=0:
                h2 = h2.next
                n-= 1
            else:
                h2 = h2.next
                h1 = h1.next
        h1.next = h1.next.next
        return h


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
res = s.deleteNoNNode(h,2)
while res:
    print(res.val)
    res= res.next