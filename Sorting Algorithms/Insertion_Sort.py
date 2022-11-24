# Insertion Sort
def insertion_sort(arr):
    swap = False
    for i in range(0, len(arr)):
        if i + 1 < len(arr):
            temp = arr[i]
            if arr[i+1] < arr[i]:
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True
            if swap == True:
                for j in reversed(range(0, i)):
                    if j - 1 >= 0:
                        if arr[j - 1] > arr[j]:
                            temp = arr[j]
                            arr[j] = arr[j - 1]
                            arr[j - 1] = temp
    return arr

    
print(f'FINAL OUTPUT : {insertion_sort([17, 31, 39, 39, 42, 15, 25, 44, 1, 35, 27, 49, 47])}')
