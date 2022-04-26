def binarysearch(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid -1
        else:
            return mid
    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
z = 8

print(binarysearch(arr, z))