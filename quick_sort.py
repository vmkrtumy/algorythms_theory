def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for num in arr[1:]:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)
        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([2, 4, 1, 3]))
