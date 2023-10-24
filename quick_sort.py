def quick(arr):
    if len(arr)>1:
        pivot = -1
        i = 0
        while i < len(arr):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                print(i)
                pivot = i
            elif arr[i] < arr[pivot]:

            print(arr)
            i+=1
        return
        left = arr[:pivot]
        right = arr[pivot:]
        quick(left)
        quick(right)
        arr = left+right
    print(arr)

quick([2, 4, 1, 3])