from engine import Engine

run = Engine([([1, 4, 0, 2, 3, 5, 0, 0, 9, 0],)]).v8

'''
iterate over the array and check if the current element is equal to zero
if it is equal to zero, increment a zero_count variable
else shift the current element down by a count equal to zero_count
'''

def move_zero1(arr: list) -> None:
    i = 0
    zero_count = 0
    n = len(arr)

    while i < n:
        if arr[i] == 0:
            zero_count += 1

        elif zero_count > 0:
            arr[i - zero_count] = arr[i]
        
        i += 1

    for i in range(n - zero_count, n):
        arr[i] = 0

run(move_zero1)

def move_zero(arr: list) -> None:
    shift = 0
    for i in range(len(arr)):
        print(arr)
        if arr[i] == 0:
            shift += 1
        elif shift > 0:
            arr[i - shift] = arr[i]
            arr[i] = 0


run(move_zero)

