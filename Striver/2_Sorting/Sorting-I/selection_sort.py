def selection_sort(arr: list) -> None:
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]    

arr = [5, 5, 8, 4, 2, 1, 9, 8, 0, 7, 5]
selection_sort(arr)
print(arr)
