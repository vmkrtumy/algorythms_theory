def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)

def heap(arr):
    res = []
    n = len(arr)
    while n != 1:
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)
        res.append(arr[0])
        arr[0] = arr[n-1]
        arr.pop()
    res.append(arr[0])
    return(res)

arr = [10, 2, 5, 12, 6, 4, 1, 13]
print(heap(arr))