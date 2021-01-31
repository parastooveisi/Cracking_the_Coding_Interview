def bubble_sort(arr):
    n = len(arr) - 1
    for i in range(n):
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort([1, 2, 8, 4, 6, 3, 7, 5]))
