def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minpos = i
        for j in range(i, n):
            if arr[j] < arr[minpos]:
                minpos = j

        arr[i], arr[minpos] = arr[minpos], arr[i]

    return arr


print(selection_sort([8, 2, 1, 4, 6, 3, 7, 5]))
