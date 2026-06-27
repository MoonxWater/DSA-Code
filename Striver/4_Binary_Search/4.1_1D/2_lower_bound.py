from engine import Engine

test_cases = [([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1], {'ret':0}),
              ([[1, 2, 3, 4, 5, 6, 7, 8, 10, 11], 9], {'ret':8})]
run = Engine(test_cases)

'''
About this problem:
'''

#----Solution----------------------------------------------------------------------

'''
have lower_bound at len of the array as fall back value
loop over the array with two variables low & high
calc mid of the two vars
if el at mid is >= given lower_bound number, we dont need the right side
    change lower_bound to mid
    move high to mid - 1
else move low to mid + 1
'''

def get_lower_bound(arr: list, target_bound) -> int:
    lower_bound = len(arr)
    low, high = 0, lower_bound - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target_bound:
            lower_bound = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return lower_bound

run.v8(get_lower_bound)