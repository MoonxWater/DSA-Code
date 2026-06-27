from engine import Engine

test_cases = [([[2, 4, 6, 8, 8, 8, 11, 13], 8], {'ret':[3, 5]}),
              ([[2, 4, 6, 8, 8, 8, 11, 13], 9], {'ret': [-1, -1]}),
              ([[2, 4, 6, 8, 8, 8, 11, 13], 11], {'ret':[6, 6]})]
run = Engine(test_cases)


'''
About this problem: given an array and a number, return the first and last occurance of the 
number in the array. if number is not present, return -1 and -1. return value should be a
list with both the pairs [first, last]
'''


#---Solution-----------------------------------------------------------------------------

'''
first:
    return -1 if array is empty
    initialise low and high to 0 and len arr - 1 and res with -1
    loop over the array till low is l-eq to high
    calc mid of low and high
    if el at mid is g-eq to target, move high to mid -1 and res to mid
    if el at mid is less than target, move low to mid + 1
    return res

last:
    return -1 if arr is empty
    initialise low and high to 0 and len arr -1 and res to -1
    loop over the array till low is l-eq to high
    calc mid of low and high
    if el at mid is l-eq to target, move low to mid + 1, store mid to res
    if el at mid is greater than target, move high to mid - 1
    return res   
'''

def first_last_occurrence(arr: list, target: int) -> list[int]:
    def first() -> int:
        if not arr:
            return -1
        
        low, high = 0, len(arr) - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                res = mid
                high = mid - 1
            
            else:
                low = mid + 1

        return res if arr[res] == target else -1

    def last() -> int:
        if not arr:
            return -1
        
        low, high = 0, len(arr) - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= target:
                res = mid
                low = mid + 1

            else:
                high = mid - 1

        return res if arr[res] == target else -1

    return [first(), last()]


def first_last_occurrence2(arr: list, target: int) -> list[int]:
    def first() -> int:
        if not arr:
            return -1
        
        low, high = 0, len(arr) - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                res = mid
                high = mid - 1
            
            elif arr[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return res

    def last() -> int:
        if not arr:
            return -1
        
        low, high = 0, len(arr) - 1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                res = mid
                low = mid + 1
            
            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return res

    return [first(), last()]

run.v8(first_last_occurrence)
run.v8(first_last_occurrence2)

run.compare(first_last_occurrence, first_last_occurrence2)