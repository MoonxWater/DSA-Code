from engine import Engine

test_cases = [([[4, 5, 1, 2, 3]], {'ret': 1}), 
              ([[2, 3, 4, 5, 6, 7]], {'ret': 2})]
run = Engine(test_cases)


'''
About this problem: you are given a rotated sorted array. return the value of the element
which is minimum.
'''


#---Solution-----------------------------------------------------------------------------

'''
initialise low and high to 0 and len - 1
keep a min var
run a loop till low <= high
check if the range arr[low] to arr[high] is sorted
if true, min is at idx low, compare with min and break. no further iteration necessary
if false, do nothing and move on with the iteration
calc mid of low and high
check which side of the array is sorted
if left side is sorted. this means minimum is on the right side
    assign the lesser val to min from min and arr[low]
    move low to mid + 1
if right side is sorted. this means minimum is on the left side
    assign the lesser val to min from min and arr[mid]
    move high to mid - 1

return min
'''

def solution(arr: list) -> int | None:
    if not arr: 
        return 
    
    low, high = 0, len(arr) - 1
    min_val = arr[0]

    while low <= high:
        if arr[low] <= arr[high]:
            min_val = min(min_val, arr[low])
            break # we break because the remaining search space is completely sorted ie works like a normal binary search problem therefore, min el will be at idx low.

        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            min_val = min(min_val, arr[low])
            low = mid + 1

        else:
            min_val = min(min_val, arr[mid])
            high = mid - 1

    return min_val


run.v8(solution)