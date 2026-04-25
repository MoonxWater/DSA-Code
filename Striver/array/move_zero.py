def move_zero1(arr: list) -> None:
    i = 0
    zero = 0
    n = len(arr)

    while i < n:
        if arr[i] == 0:
            zero += 1

        else:
            arr[i - zero] = arr[i]
        
        i += 1

    for i in range(n - zero, n):
        arr[i] = 0

arr = [1, 4, 0, 2, 3, 5, 0, 0, 9, 0]
move_zero1(arr)
print(arr)


def move_zero(arr: list) -> None:
    shift = 0
    for i in range(len(arr)):
        print(arr)
        if arr[i] == 0:
            shift += 1
        elif shift > 0:
            arr[i - shift] = arr[i]
            arr[i] = 0  # fill zero immediately, no second pass needed


arr = [1, 4, 0, 2, 3, 5, 0, 0, 9, 0]
move_zero(arr)
print(arr)

