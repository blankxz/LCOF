def binarySearch(a,target):
    left = 0
    right = len(a)-1
    while left<=right:
        temp = left+(right-left)//2
        if a[temp]<target:
            left = temp+1
        elif a[temp]>target:
            right = temp-1
        else:
            return temp

def binarySearchLeft(arr,target):
    left = 0
    right = len(arr)
    while left<right:
        temp = left+(right-left)//2
        if arr[temp] == target:
            right = temp
        elif arr[temp] > target:
            right = temp
        elif arr[temp] < target:
            left = temp+1
    return left

def binarySearchRight(arr,target):
    left = 0
    right = len(arr)
    while left<right:
        temp = left+(right-left)//2
        if arr[temp] == target:
            left = temp+1
        elif arr[temp] > target:
            right = temp
        elif arr[temp] < target:
            left = temp+1
    return left-1

print(binarySearchLeft([1,2,3,4,4,4,4,4,4,4,4,6],4))
print(binarySearchRight([1,2,3,4,4,4,4,4,4,4,4,6],4))
binarySearch([1,2,3,4,5,6,7,8,9],1)