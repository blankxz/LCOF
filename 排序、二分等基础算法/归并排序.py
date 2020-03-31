def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def mergeSort(arr):
    if len(arr)<2:
        return arr
    m = len(arr)//2
    left,right = arr[0:m], arr[m:]
    res_left = mergeSort(left)
    res_right = mergeSort(right)
    return merge(res_left,res_right)

a = [2,8,9,10,4,5,6,7]
a = mergeSort(a)
print(a)
