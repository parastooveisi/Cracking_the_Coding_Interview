def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    result = []
    l_index = r_index = 0

    while l_index < len(left_arr) and r_index < len(right_arr):
        if left_arr[l_index] < right_arr[r_index]:
            result.append(left_arr[l_index])
            l_index += 1

        else:
            result.append(right_arr[r_index])
            r_index += 1

    result.extend(left_arr[l_index:])
    result.extend(right_arr[r_index:])

    return result


print(merge_sort([8, 2, 1, 4, 6, 3, 7, 5, 12, 10]))
