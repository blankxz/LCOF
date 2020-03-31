def selectSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

a = [2,8,9,10,4,5,6,7]
selectSort(a)
print(a)
