def interpolation_search(arr_list, key):
    arr_list.sort()
    is_found = False
    low = 0
    high = len(arr_list) - 1
    while not is_found and key in arr_list:
        pos = int(low + ((key - arr_list[low]) * (high - low) / (arr_list[high] - arr_list[low])))
        if arr_list[pos] == key:
            print(f"ELEMENT FOUND AT {pos}")
            is_found = True
        elif arr_list[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    if not is_found:
        print("ELEMENT NOT FOUND")


interpolation_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 765], 34)
