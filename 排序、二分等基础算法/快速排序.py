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


a = [2,8,9,10,4,5,6,7]
print(quickSort(a))