from engine import Engine
# from engine_legacy import Engine

test_cases = [
    ([[1, 2, 0, 1, 1, 2, 2, 1, 2, 1, 0, 0, 0, 2, 1, 0, 2, 0, 2, 0]], {"mod":[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]}),
    ([[2, 1, 0, 1, 0, 2, 0]], {"mod":[0, 0, 0, 1, 1, 2, 2]}),
    ([[1, 0]], {"mod":[0, 1]})
    ]

run = Engine(test_cases)

'''
Better:
iteration over the array and store the count of all three numbers
do a second iteration and overwrite the elements according to their cnts
'''

def sort_0_1_2_better(arr: list) -> None:
    cnt_0 = 0
    cnt_1 = 0

    for num in arr:
        if num == 0:
            cnt_0 += 1
        
        elif num == 1:
            cnt_1 += 1
        
    for i in range(len(arr)):
        if i < cnt_0:
            arr[i] = 0
        elif i < cnt_0 + cnt_1:
            arr[i] = 1
        else:
            arr[i] = 2

'''
This algorithm has 3 rules:
    1. from 0 to low - 1 -> all 0
    2. from low to mid - 1 -> all 1
    3. from high + 1 to n - 1 -> all 2
    Note: from mid to high -> unsorted
initialise 3 variables: low, mid and high to 0, 0 and n - 1
iterate over the array and check value of current element
use while loop with condition mid <= high
    if mid == 0 swap with element at low and increment both
    elif mid == 1 increment mid
    else swap with high and decrement high
'''

def dutch_national_flag_algo(arr: list) -> None:
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1 
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1
        
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# run.v8(sort_0_1_2_better)
run.v8(dutch_national_flag_algo)


        