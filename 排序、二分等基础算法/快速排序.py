def quickSort(arr):
     if len(arr)<2:
         return arr
     key_ind = len(arr)//2
     key = arr[key_ind]
     left, right = [], []
     arr.pop(key_ind)
     for i in arr:
         if i > key :
             right.append(i)
         else:
             left.append(i)
     return quickSort(left)+[key]+quickSort(right)


def quickSort2(arr,left,right):
    if left>right:
        return
    temp = arr[left]
    l = left
    r = right
    while l!=r:
        while arr[r]>=temp and l<r:
            r-=1
        while arr[l]<=temp and l<r:
            l+=1
        if l<r:
            arr[l],arr[r] = arr[r],arr[l]
    arr[left],arr[l] = arr[l],arr[left]
    quickSort2(arr,left,l-1)
    quickSort2(arr,l+1,right)

a = [2,8,9,10,4,5,6,7]
# print(quickSort(a))

quickSort2(a,0,len(a)-1)
print(a)
import sys
a = 1
print(sys.getsizeof(a))