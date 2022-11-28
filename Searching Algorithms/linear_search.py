def linear_search(arr, ele):
    for i in range(0, len(arr)):
        if arr[i] == ele:
            return i
    return -1

index = linear_search([12,541,5,23,7675,34,1213,65,434,24,675,53,7,87,554,76], 554)
print(f'Element found at {index}' if index != -1 else 'Element Not found')
