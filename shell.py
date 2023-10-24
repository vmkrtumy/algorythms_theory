def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    input_list = [12, 34, 54, 2, 3]
    print("Original list:", input_list)
    
    shell_sort(input_list)
    
    print("Sorted list:", input_list)
