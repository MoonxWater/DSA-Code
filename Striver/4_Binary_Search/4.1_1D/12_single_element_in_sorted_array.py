from engine import Engine

test_cases = [([[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]], {'ret': 4}), 
              ([[1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]], {'ret': 1}),
              ([[1]], {'ret': 1}),
              ([[]], {'ret': None})]
run = Engine(test_cases)


'''
About this problem: Given a sorted array, we have to return the only number that appears
once while all the other numbers appear twice.
'''


#---Solution-----------------------------------------------------------------------------

'''
initialise two variables low and high to 0 and len - 1
run a loop till low <= high
calc mid of low and high
access the el at mid
if the el at mid - 1 is equal to el at mid
    if (mid + 1) % 2 == 0: our number is not in the left half, eliminate it: low = mid + 1
    else: our element is in the left half: high = mid - 1
elif the el at mid + 1 is equal to el at mid
    if (mid + 2) % 2 == 0: our number is not in the right half, eliminate it: low = mid + 1 
    else: our element is in the right half: high = mid - 1
else:
    the el at mid is the element itself: return it
'''

def solution1(arr: list) -> int | None:
    if len(arr) == 1:
        return arr[0]
    
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if mid > 0 and arr[mid] == arr[mid - 1]:
            if (mid + 1) % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1
        
        elif mid < len(arr) - 1 and arr[mid] == arr[mid + 1]:
            if (mid + 2) % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1

        else:
            return arr[mid]
        
    return None


'''
a better approach would be to first check if el at 0 and len - 1 is the required one
if not, we can trim the search space by one from both sides and save conditions
to decide which side of the array we are on, we need to look how the elements arrange when the 
required number is crossed and when it is not crossed.
the pairs are arranged as (even, odd) pairs before the single element
and when the element is crossed, the pairs become (odd, even), using this, we can successfully 
eliminate half of the search space at each iteration.
'''

def solution2(arr: list) -> int | None:
    if not arr:
        return None
    
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] != arr[1]:
        return arr[0]
    
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    low, high = 1, len(arr) - 2

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            low = mid + 1

        else: 
            high = mid - 1

    return None

run.v8(solution1)
run.v8(solution2)