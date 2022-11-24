# Insertion Sort
def insertion_sort(arr):
    swapped = False
    for i in range(0, len(arr)):
        if i + 1 < len(arr):
            if arr[i+1] < arr[i]:
                arr = swap(i, i+1, arr)
                swapped = True
            if swapped == True:
                for j in reversed(range(0, i)):
                    if j - 1 >= 0:
                        if arr[j - 1] > arr[j]:
                            arr = swap(j, j-1, arr)
    return arr


def swap(current_index,next_index, arr):
    temp = arr[current_index]
    arr[current_index] = arr[next_index]
    arr[next_index] = temp
    return arr

    
print(f'FINAL OUTPUT : {insertion_sort([17, 31, 39, 39, 42, 15, 25, 44, 1, 35, 27, 49, 47])}')
