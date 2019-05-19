def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


array = list(map(int, input().split()))
print(' '.join(map(str, bubble_sort(array))))
