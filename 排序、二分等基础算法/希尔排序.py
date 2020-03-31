def shellSort(arr):
    gap = 1
    while gap<len(arr)/3:
        gap = gap*3+1
    while gap>0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j>= 0 and arr[j]>temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = gap//3

a = [2,8,9,10,4,5,6,7]
shellSort(a)
print(a)
