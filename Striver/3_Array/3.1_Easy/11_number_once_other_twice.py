from engine import Engine


'''
About this problem: 
'''

test_cases = [
    ([[1, 1, 2, 3, 3, 4, 4]], {'ret': None}),
    ([[6, 7, 5, 4, 1, 2, 3, 8, 8, 6, 5, 7, 3, 2, 1]], {'ret': None}),
    ([[1, 1, 4, 5, 4, 3, 0, 2, 2, 3, 5]], {'ret': None})
]
run = Engine(test_cases)

#---Solution-----------------------------------------------------------------------------

'''

'''

def solution():
    ...


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



'''the xor approch
xor is difference checker ie if both inputs are same -> 0, unique -> some number
xor of a number with 0 is the number itself.

the approach uses this property by storing a varible and xoring each element of the input array
by the variable.
if all numbers are in pairs, they will cancel each other out since xor does not depend on order
That one number which appears once will not cancel out and be returned as the result.
'''

def appear_once2(arr: list) -> int:
    '''Returns -1 if there is no number appearing once'''

    if len(arr) % 2 == 0:
        raise ValueError("No number appears once")
    
    xor = 0

    for i in range(len(arr)):
        xor ^= arr[i]

    return xor


run.v8(appear_once)
run.v8(appear_once2)

run.compare(appear_once, appear_once2)