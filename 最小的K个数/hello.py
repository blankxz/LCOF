class Solution:
    def getLeastNumbers(self, arr, k: int):
        def partation(l,r,arr,k):
            if arr == []:
                return
            if l>=r:
                return
            key = arr[l]
            left = l
            right = r
            while left!=right:
                while arr[right]>= key and left<right:
                    right-=1
                while arr[left]<=key and left<right:
                    left+=1
                if left<right:
                    arr[left],arr[right] = arr[right],arr[left]
            arr[left],arr[l] = arr[l],arr[left]
            if left == k-1:
                return
            partation(l,left-1,arr,k)
            partation(left+1,r,arr,k)

        partation(0,len(arr)-1,arr,k)
        print(arr)
        return arr[:k]
            
            
s = Solution()
print(s.getLeastNumbers([3,2,1],2))