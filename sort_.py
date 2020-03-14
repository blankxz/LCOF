
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble([3,6,8,1,2,10,5]))

def select(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        if min_ind != i:
            arr[i],arr[min_ind] = arr[min_ind],arr[i]
    return arr
print(select([3,6,8,1,2,10,5]))

def insert(arr):
    for i in range(len(arr)):
        preind = i-1
        cur = arr[i]
        while preind >=0 and arr[preind]>cur:
            arr[preind+1] = arr[preind]
            preind -= 1
        arr[preind+1] = cur
    return arr
print(insert([3,6,8,1,2,10,5]))

