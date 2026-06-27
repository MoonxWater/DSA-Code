from engine import Engine

test_cases = [([[1, 1, 1, 2, 2, 3, 3], 3], {'ret': 2}), 
              ([[1, 1, 3, 3, 3, 4, 5, 6, 7, 7, 9], 2], {'ret': 0})]
run = Engine(test_cases)


'''
About this problem: count occurrences of the given number from the given array
'''


#---Solution-----------------------------------------------------------------------------

'''
get first occurrence via binary search
get last occurrence via binary search
total occurrences is equal to last - first + 1
'''

def count_occurrences1(arr: list, target: int) -> int:
    if not arr:
        return 0
    
    def first() -> int:
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
    
    res1 = first()
    
    if res1 == -1: return 0
    
    res2 = last()

    return res2 - res1 + 1

run.v8(count_occurrences1)