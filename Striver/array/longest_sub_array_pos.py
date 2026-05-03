from engine import Engine

test_cases = (([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3), 
              ([3, 1, 1, 1, 3], 3), 
              ([1, 2, 1, 0, 1, 1, 0], 2))
run = Engine(*test_cases).v8

'''
iterate and store a running sum and store unique ones in a dict with value and index
at each iteration, check if there exists in the dict a sum of X(running sum) - k(the given value)
if it exists, the remaining subarray must have a sum of k. 
check if the size if greater than what the prev size was.
return the size
'''

def longest_subarray(arr: list, k: int) -> int:
    '''
    For positives, negatives and zeros.
    '''

    max_size = 0
    summations = {}
    running_sum = 0

    for i in range(len(arr)):
        running_sum += arr[i]

        if running_sum == k:
            max_size = max(max_size, i + 1)

        else: 
            if (idx := summations.get(running_sum - k)) is not None:
                max_size = max(max_size, i - idx)

        if running_sum not in summations:
            summations.update({running_sum: i})    

    return max_size

run(longest_subarray)