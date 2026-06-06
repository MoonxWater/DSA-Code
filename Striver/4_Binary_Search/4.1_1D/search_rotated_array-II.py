from engine import Engine

test_cases = [([[7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 3], {'ret': True}), 
              ([[3, 1, 2, 3, 3, 3, 3], 4], {'ret': False})]
run = Engine(test_cases)


'''
About this problem: same as the search sorted and rotated array problem but here, there can be 
duplicates within the array.
'''


#---Solution-----------------------------------------------------------------------------

'''
the solution is the same as the type 1 problem
initialise low and high to 0 and len - 1
run a loop till low <= high
calc mid of low and high
check if el at mid is target, if true, return True
check if arr[low] == arr[mid] == arr[high] (edge case) # this is the reason we cannot copy paste type 1 sol
    if true, trim search space by one from each side as this number will not be equal to target
    (courtesy of prev if statement)
rest is same
check which half is sorted
arr[low] <= arr[mid]
    if true, check if target in range arr[low] to arr[mid] exclusive
        if true, move high to mid - 1
        if false, move low to mid + 1
    if false, check if target in range arr[mid] exclusive to arr[high]
        if true, move low to mid + 1
        if false, move high to mid - 1

return False as fallback value
'''

def search_sorted_rotated_array_with_duplicates(arr: list, target: int) -> bool:
    if not arr: 
        return False
    
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        
        if arr[low] == arr[mid] == arr[high]:
            low, high = low + 1, high - 1

        if arr[low] <= arr[mid]:
            if arr[low] <=target < arr[mid]:
                high = mid - 1
            
            else:
                low = mid + 1

        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1

            else:
                high = mid - 1
        
    return False


run.v8(search_sorted_rotated_array_with_duplicates)