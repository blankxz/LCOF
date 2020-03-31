def bucketSort(arr):
    maximum, minimum = max(arr), min(arr)
    bucketArr = [[] for i in range(maximum // 10 - minimum // 10 + 1)]  # set the map rule and apply for space
    for i in arr:  # map every element in array to the corresponding bucket
        index = i // 10 - minimum // 10
        bucketArr[index].append(i)
    arr.clear()
    for i in bucketArr:
        i.sort()   # sort the elements in every bucket
        arr.extend(i)  # move the sorted elements in bucket to array

a = [2,8,9,10,4,5,6,7]
bucketSort(a)
print(a)