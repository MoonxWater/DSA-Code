from engine import Engine

test_cases = [([[10, 20, 30, 40, 50], 25], {'ret':30}), ([[10, 20, 25, 30, 40], 25], {'ret':25})]
run = Engine(test_cases)


'''
About this problem: given an array, return the smallest num g-eq to given num x
uf not found, return -1
'''


#---Solution-----------------------------------------------------------------------------

'''
return -1 if arr is empty
initialise low and high to 0 and len arr -1
initialise ceil to -1
loop over the arr while low is l-eq to high
calc mid of low and high
check if el at mid if equal to target
if yes, return arr[mid]
if el at mid is greater than target, update ceil to arr[mid], move high to mid -1
if el at mid is less than target, move low to mid + 1
return ceil
'''

def get_ceil(arr: list, target: int) -> int:
    if not arr:
        return -1
    
    low, high = 0, len(arr) - 1
    ceil = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]
        
        elif arr[mid] > target:
            ceil = arr[mid]
            high = mid - 1

        else:
            low = mid + 1

    return ceil

run.v8(get_ceil)