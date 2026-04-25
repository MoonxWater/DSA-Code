from engine import run

test_cases = (([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3), ([3, 1, 1, 1, 3], 3), ([1, 2, 1, 0, 1, 1, 0], 2))

'''
we have to return the longest subarray with elements summing up to k
one variable to store the max_size, one to store cur_size
one idx variable to store the start of the subarray
one pointer that will traverse through the array
'''

def longest_subarray(arr: list, k: int) -> int:
    max_size = cur_size = sm= 0
    i = 0

    while i < len(arr):
        if sm + arr[i] > k:
            max_size = max(cur_size, max_size)
            sm = cur_size = 0
        else:
            sm += arr[i]
            cur_size += 1
            i += 1

    return max(cur_size, max_size)

# run(longest_subarray, *test_cases)

print(longest_subarray([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3))