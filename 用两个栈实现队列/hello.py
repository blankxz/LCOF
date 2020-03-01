class CQueue:

    def __init__(self):
        self.val1,self.val2 = [], []

    def appendTail(self, value: int) -> None:
        self.val1.append(value)

    def deleteHead(self) -> int:
        if self.val2:
            return self.val2.pop()
        if self.val1 == []:
            return -1
        else:
            while self.val1 != []:
                self.val2.append(self.val1.pop())
            return self.val2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()