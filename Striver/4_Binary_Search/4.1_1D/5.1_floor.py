from engine import Engine

test_cases = [([[10, 20, 30, 40, 50], 25], {'ret':20}), ([[10, 20, 25, 30, 40], 25], {'ret':25})]
run = Engine(test_cases)


'''
About this problem: given an array, return the largest number which is l-eq to given num x.
If not found, return -1
'''


#---Solution-----------------------------------------------------------------------------

'''
return -1 if arr is empty
initialise low and high to 0 and len arr -1
initialise floor to -1
loop over the arr till low is l-eq to high
calc mid of low and high
if el at mid is equal to target
return arr[mid]
if el at  mid is < target, update floor to el at mid
move low to mid + 1
if el at mid is > target, update high to mid - 1
return floor
'''

def get_floor(arr: list, target: int) -> int:
    if not arr:
        return -1
    
    low, high = 0, len(arr) - 1
    floor = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]
        
        elif arr[mid] < target:
            floor = arr[mid]
            low = mid + 1

        else:
            high = mid - 1

    return floor


run.v8(get_floor)