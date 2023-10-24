nums = [1, 5, 6, 12, 34, 56, 67, 89, 90]
value = 6

def binary_search(nums, vlaue):
    low = 0
    high = len(nums)- 1
    mid = high//2
    if value > nums[high] or value < nums[low]:
        return False
    temp = []
    if nums[mid] == value:
        return True
    elif nums[mid] < value:
        temp = nums[mid+1:high+1]
        t = binary_search(temp, value)
    else:
        temp = nums[low:mid]
        t = binary_search(temp, value)
    if t:
        return True
    else:
        return False
print(binary_search(nums, value))