from engine import Engine

test_cases = [([[3, 4, 5, 1, 2]], {'ret': 3}), 
              ([[6, 7, 8, 9, 1, 2]], {'ret': 4})]
run = Engine(test_cases)


'''
About this problem: given an array, return the number of time the array has been rotated
eg: [3, 4, 5, 1, 2] has been rotated 3 times bcz there are 3 elements before pivot (point of rotation)
'''


#---Solution-----------------------------------------------------------------------------

'''
get the minimum element in the array and return its index which would be equal to the number of rotations.
initilise low and high to 0 and len - 1 
keep a idx varible with default value as 0
run a loop till low <= high
insert early exit by checking if the array is sorted in the range low to high
    compare arr[idx] with arr[low] and break
calc mid of low and high
check which side is sorted
if left half is sorted
    compare arr[idx] with arr[low] and assign the smaller's index to idx
    move low to mid + 1
if right half is sorted
    compare arr[idx] with arr[mid] and assign the smaller's index to idx
    move high to mid - 1
return idx
'''

def solution(arr: list) -> int:
    if not arr:
        return 0
    
    low, high = 0, len(arr) - 1
    idx = 0

    while low <= high:
        if arr[low] <= arr[high]:
            idx = low if arr[low] < arr[idx] else idx
            break

        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            idx = low if arr[low] < arr[idx] else idx
            low = mid + 1
        
        else:
            idx = mid if arr[mid] < arr[idx] else idx
            high = mid - 1

    return idx


run.v8(solution)