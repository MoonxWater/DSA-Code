def left_rotate(arr: list, k: int) -> None:
    n = len(arr)
    k = k % len(arr)
    arr.reverse()

    arr[:n - k] = sorted(arr[:n - k]) 
    arr[n - k:] = sorted(arr[n - k:])
    

arr = [1, 2, 3, 4, 5, 6, 7, 8]
left_rotate(arr, 5)
print(arr)