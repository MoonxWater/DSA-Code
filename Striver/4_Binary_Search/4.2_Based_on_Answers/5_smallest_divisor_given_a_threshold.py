from engine import Engine

test_cases = [([[1, 2, 5, 9], 6], {'ret': 5}), 
              ([[8,4,2,3], 10], {'ret': 2}), 
              ([[1,2,3,4,5], 8], {'ret': 3})]
run = Engine(test_cases)


'''
About this problem: given an array and a threshold, return the smallest number that which divides 
each element of the array and then ceiled and then summed, is smaller than the threshold.
'''


#---Solution-----------------------------------------------------------------------------

'''
return -1 if the len of the array is greater than the threshold
initialise low and high to 1 and max of nums

run a loop while low <= high
calc mid of low and high
make a cur_sum var

run a for loop inside the while loop and iterate over the nums array
divide the current element with mid and ceil it, add the result to cur_sum var.
outside the for loop,
if the cur_sum is <= the threshold, we have a possible answer, high to mid - 1
else, the divisor needs to be increased in order for the results to be smaller, low to mid + 1

return low
'''

def solution(nums: list, threshold: int) -> int:
    if len(nums) > threshold:
        return -1 
    
    low, high = 1, max(nums)

    while low <= high:
        mid = (low + high) // 2
        cur_sum = 0

        for num in nums:
            cur_sum += (num + mid - 1) // mid

        if cur_sum <= threshold:
            high = mid - 1

        else:
            low = mid + 1

    return low

run.v8(solution)

from random import randint
run.scale(solution, lambda n: [[randint(-10, 10) for _ in range(n)], 5])