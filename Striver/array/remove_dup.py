def remove_dup(arr: list) -> None:
    if len(arr) == len(set(arr)):
        return
    
    offset = 0

    for i in range(1, len(arr)):
        if arr[i - offset] == arr[i - 1 - offset]:
            arr.pop(i - offset)
            offset += 1
    

arr = [1, 1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 9, 9]
remove_dup(arr)
print(arr)