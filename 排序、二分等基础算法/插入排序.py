def insertSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        curIndex = arr[i]
        while preIndex > 0 and arr[preIndex] > curIndex:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = curIndex
    return arr

a = [2,8,9,10,4,5,6,7]
insertSort(a)
print(a)
