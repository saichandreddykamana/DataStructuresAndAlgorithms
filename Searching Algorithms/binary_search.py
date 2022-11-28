import math
def binary_search(arr, low, high, ele):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
           return binary_search(arr, low, mid - 1, ele)
        elif arr[mid] < ele:
            return binary_search(arr, mid + 1, high, ele)
    return -1
arr = [12,541,5,23,7675,34,1213,65,434,24,675,53,7,87,554,76]
arr.sort()
index = binary_search(arr,0, len(arr) -1, 554)
print(f'Element found at {index}' if index != -1 else 'Element Not found')
