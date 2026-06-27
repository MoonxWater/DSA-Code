from engine import Engine

test_cases = []
run = Engine(test_cases)

'''

'''


#---Solution--------------------------------------------------------------------------------

'''

'''

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

arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
left_rotate(arr1, 5)
print(arr1)


'''

'''

def left_rotate2(arr: list, k: int) -> None:
    n = len(arr)
    k = k % len(arr)
    arr.reverse()

    arr[:n - k] = sorted(arr[:n - k]) 
    arr[n - k:] = sorted(arr[n - k:])
    

arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
left_rotate2(arr2, 5)
print(arr2)

print(arr1==arr2)