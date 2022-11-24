# Bubble Sort

def bubble_sort(arr):
    print(f"INPUT : {arr}")
    swaped = True
    while swaped:
        swaped = False
        for i in range(0, len(arr)):
            if i + 1 <= len(arr) - 1:
                if arr[i+1] < arr[i]:
                    arr = swap(i, i+1, arr)
                    swaped = True
        print(f"{arr}")
    return arr

def swap(current_index, next_index, arr):
    temp = arr[current_index]
    arr[current_index] = arr[next_index]
    arr[next_index] = temp
    return arr

    
print(f'FINAL OUTPUT : {bubble_sort([17, 31, 39, 39, 42, 15, 25, 44, 1, 35, 27, 49, 47])}')
