from engine import Engine

test_cases = [([[4, 5, 6, 7, 0, 1, 2], 3], {'ret': -1}), 
              ([[4, 5, 6, 7, 0, 1, 2], 0], {'ret': 4}),
              ([[3,4,5,6,7,1,2], 7], {'ret': 4}), 
              ([[3, 1], 1], {'ret': 1})]
run = Engine(test_cases)


'''
About this problem: an array is sorted and then rotated. search for the given number and return its
index. if not found, return -1
'''


#---search_sorted_rotated_array-----------------------------------------------------------------------------

'''
have two variables low and high at idx 0 and len - 1
run a loop till low <= high
calc mid of these two
check whether el at mid is target, return mid if true
check which half is sorted by by doing arr[low] <= arr[mid]
    then check if target lies in the range arr[low] to arr[mid] exclusive
    if true, move high to mid -1
    if false, move low to mid +1
if right half is sorted
    then check if target lies in the range arr[mid] exclusive to arr[high]
    if true, move low to mid +1
    if false, move high to mid -1
return -1 as fallback value
'''

def search_sorted_rotated_array(arr: list, target: int) -> int:
    if not arr:
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1  

            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            
            else:
                high = mid - 1

    return -1

run.v8(search_sorted_rotated_array)