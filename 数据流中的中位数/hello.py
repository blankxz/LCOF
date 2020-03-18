
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
        else:
            ind = self.binary(0,len(self.arr),self.arr,num)
            self.arr.insert(ind, num)
            # print(self.arr)

    def binary(self,l,r,arr,tar):
        while l <r :
            mid = l+(r-l)//2
            if arr[mid] == tar:
                return mid
            if arr[mid] > tar:
                r = mid
            if arr[mid]<tar:
                l = mid +1
        return l
        
        

    def findMedian(self) -> float:
        if len(self.arr)%2 == 0:
            return (self.arr[len(self.arr)//2]+self.arr[len(self.arr)//2-1])/2
        else:
            return self.arr[len(self.arr)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()