def selection_sort(nums):
    i = k = 0
    while i < len(nums):
        minn = i
        j = i+1
        while j < len(nums):
            if nums[j] < nums[minn]:
                minn = j
            j+=1
        nums[k], nums[minn] = nums[minn], nums[k]
        i+=1
        k+=1
    print(nums)

selection_sort([2, 0, 2, 3, 3, 4])