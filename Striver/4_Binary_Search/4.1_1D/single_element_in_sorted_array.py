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

        if arr[mid] == arr[mid - 1]:
            if (mid + 1) % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1
        
        elif arr[mid] == arr[mid + 1]:
            if (mid + 2) % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1

        else:
            return arr[mid]
        
    return None




run.v8(solution1)