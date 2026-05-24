from engine import Engine

test_cases = [([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1], {'ret':0}),
              ([[1, 2, 3, 4, 5, 6, 7, 8, 10, 11], 9], {'ret':7}),
              ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3], {'ret':2})]
run = Engine(test_cases)

'''
About this problem
'''

#---Solution-------------------------------------------------------------------

'''
upper bound var with initial value set to idx 0
two pointers low and high
loop over the array and calc mid of low and high
check if el at mid is <= given upper bound 
if true, update upper_bound to mid
    move low to mid + 1
else move high to mid - 1
return upper_bound
'''

def get_upper_bound(arr: list, target_bound: int) -> int:
    if not arr:
        return -1
    
    upper_bound = -1
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= target_bound:
            upper_bound = mid
            low = mid + 1
        else:
            high = mid - 1

    return upper_bound


run.v8(get_upper_bound)