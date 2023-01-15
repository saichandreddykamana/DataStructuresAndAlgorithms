import math


def jump_search(arr_list, ele):
    arr_list.sort()
    print("LIST : ", arr_list)
    print("LIST LENGTH : ", len(arr_list))
    jump_gap = math.ceil(math.sqrt(len(arr_list)))
    print("JUMP GAP : ", jump_gap)
    current_index = 0
    while current_index <= len(arr_list):
        if current_index == -1:
            print("ELEMENT NOT FOUND")
            break
        elif arr_list[current_index] == ele:
            print(f"ELEMENT FOUND AT : {current_index}")
            break
        elif current_index + jump_gap <= len(arr_list):
            current_index += jump_gap
            if arr_list[current_index] > ele:
                current_index = find_element(arr_list=arr_list, start=current_index, end=current_index - jump_gap, ele=ele)

        else:
            current_index = find_element(arr_list=arr_list, start=len(arr_list) - 1, end=len(arr_list) - 1 - jump_gap, ele=ele)


def find_element(arr_list, start, end, ele):
    for i in range(start, end, -1):
        if arr_list[i] == ele:
            return i
    return -1


jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 765], 610)
