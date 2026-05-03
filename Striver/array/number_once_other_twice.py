'''
we can also add a pre check -> len(num) % 2 == 0: all are pairs
loop through the array with step 2.
at each step, check if num[i] != num[i + 1]: return num[i]
'''

def appear_once(arr: list) -> int:
    if len(arr) % 2 == 0:
        raise ValueError("No number appears once")
    
    for i in range(0, len(arr), 2):
        if arr[i] != arr[i + 1]:
            return arr[i]
        
    raise ValueError("No number appears once")

arr = [1, 1, 2, 3, 3, 4, 4]

# print(appear_once(arr))


'''the xor approch'''

def appear_once2(arr: list) -> int:
    '''Returns -1 if there is no number appearing once'''

    if len(arr) % 2 == 0:
        raise ValueError("No number appears once")
    
    xor = 0

    for i in range(len(arr)):
        xor ^= arr[i]

    return xor

arr = [1, 1, 2, 3, 3, 4, 4]
arr2 = [6, 7, 5, 4, 1, 2, 3, 8, 8, 6, 5, 7, 3, 2, 1]
arr3 = [1, 1, 4, 5, 4, 3, 0, 2, 2, 3, 5]
# print(appear_once2(arr))
# print(appear_once2(arr2))
# # print(appear_once2([-1, 2, 4, 3, 1, -1, 4, 3, 2, 1]))
# print(appear_once2(arr3))
from engine import Engine
run = Engine((arr,), (arr2,), (arr3,)).v8

run(appear_once2)