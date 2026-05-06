def left_rotate(arr: list, k: int):
    k = k % len(arr)
    
    i = 0

    while i < len(arr) - k: 
        for j in range(k):
            try:
                arr[i + j], arr[i + j + k] = arr[i + j + k], arr[i + j]
            except IndexError:
                print(i, j, k)
        i += k

arr = [1, 2, 3, 4, 5, 6, 7, 8]
left_rotate(arr, 5)
print(arr)


def left_rotate2(arr: list, k: int) -> None:
    n = len(arr)
    k = k % len(arr)
    arr.reverse()

    arr[:n - k] = sorted(arr[:n - k]) 
    arr[n - k:] = sorted(arr[n - k:])
    

arr = [1, 2, 3, 4, 5, 6, 7, 8]
left_rotate2(arr, 5)
print(arr)