def heapify(tree,n,i):
    if i >= n:
        return
    c1 = 2*i + 1
    c2 = 2*i + 2
    max_ind = i
    if c1 < n and tree[c1] > tree[max_ind]:
        max_ind = c1
    if c2 < n and tree[c2] > tree[max_ind]:
        max_ind = c2
    if max_ind != i:
        tree[max_ind],tree[i] = tree[i],tree[max_ind]
        heapify(tree,n,max_ind)

def buildHeap(tree,n):
    last_node = n-1
    parent = (last_node-1)//2
    for i in range(parent,-1,-1):
        heapify(tree,n,i)

def heapSort(tree,n):
    if not tree:
        return []
    buildHeap(tree,n)
    tree[n-1],tree[0] = tree[0],tree[n-1]
    return [tree[n-1]]+heapSort(tree[:-1],n-1)

tree_ = [4,10,3,5,1,2]
n_ = len(tree_)
print(heapSort(tree_,n_))