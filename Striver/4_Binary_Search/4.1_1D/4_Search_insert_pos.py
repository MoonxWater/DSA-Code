from engine import Engine

test_cases = [([[1, 2, 4, 7], 6], {'ret':3}),
              ([[1, 2, 4, 7], 8], {'ret':4}),
              ([[2, 3, 4, 7], 1], {'ret':0})]
run = Engine(test_cases)


'''
About this problem: you are given a number. search for the index of the number in a sorted 
array. If found, return the index of the array. If not found, return the index where it should be
inserted to maintain the sorted property.
'''


#---Solution-----------------------------------------------------------------------------

'''
return 0 if array is empty
initialise low and high to 0 and len array -1
initialise insert_pos variable to len of array (case where no pos is found in which case insert last)
loop over the array while low is l-eq to high.
calc the mid of low and high
check if el at mid is equal to target
if yes, return mid
elif el at mid is less than target, move low to mid + 1, 
else, move high to mid - 1 and update insert_pos to mid
return insert_pos
'''

def insert_position(arr: list, target) -> int:
    if not arr:
        return 0
    
    low, high = 0, len(arr) - 1
    insert_pos = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1

        else:
            insert_pos = mid
            high = mid - 1

    return insert_pos


run.v8(insert_position)