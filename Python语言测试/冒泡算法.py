def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

arr = bubbleSort([3,1,5,7,2,1,1,1,5,5,5])
print(arr)
