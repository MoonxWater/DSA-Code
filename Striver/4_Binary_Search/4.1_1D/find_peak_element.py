from engine import Engine

test_cases = [([[1, 2, 3, 4, 5, 6, 7, 8, 5, 1]], {'ret': 8}), 
              ([[1, 2, 1, 3, 5, 6, 4]], {'ret': 6})]
run = Engine(test_cases)


'''
About this problem: Given an array, return any peak element. A peak element is an element that is 
strictly greater than its neighbours. If there is no peak, return the greatest number (it would be
the first element in a decreasing slope and the last element in an increasing slope)
'''

r'''
Intuition:
|     ^                   
|   /   \              
|  /     \               
| /       \            
|____________
in a single peak array, there are only 3 possible cases that the mid can end up on
the increasing half
the peak
the decreasing half
if the mid is peak, perfect return
if mid is on increasing half, we dont need the left half as no peak is there
if mid is on the decreasing half, we dont need the right half as no peak is there

in multiple peak array
|     ^                 ^   
|   /   \      ^      /   \   
|  /     \   /   \   /     \      
| /       \ /     \ /       \   
|____________________________
there are 4 possible pos for mid
the increasing half
the peak
the pit
the decreasing half

return el at mid if peak
eliminate the left half if increasing
eliminate the right half if decreasing
eliminate any half if pit
'''
#---Solution-----------------------------------------------------------------------------

'''
do separate checks for the boundary elements
initialise low and high to 1 and len - 2
run a loop till low <= high
calc mid of low and high

if arr[mid] is strictly greater than both its neighbours, return arr[mid]
if arr[mid] > arr[mid - 1], it is increasing half, eliminate the left half
else eliminate the right half
'''

def solution(arr: list) -> int | None:
    if not arr: 
        return None
    
    if len(arr) == 1 or arr[0] > arr[1]:
        return arr[0]
    
    if arr[-1] > arr[-2]:
        return arr[-1]
    
    low, high = 1, len(arr) - 2

    while low <= high: 
        mid = (low + high) // 2

        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return arr[mid]
        
        elif arr[mid - 1] < arr[mid]:
            low = mid + 1

        else:
            high = mid - 1


run.v8(solution)