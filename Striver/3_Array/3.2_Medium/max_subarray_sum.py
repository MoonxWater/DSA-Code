from engine import Engine

test_cases = [([[-2, -3, 4, -1, -2, 1, 5, -3]], {"ret":7}),
               ([[5,4,-1,7,8]], {"ret":23}), 
               ([[-2,1,-3,4,-1,2,1,-5,4]], {"ret":6}), 
               ([[3, -100, 4]], {"ret":4})]
run = Engine(test_cases)

'''About this problem'''


# ----Solutions------------------------------------------------------


'''Since learning Moore's voting algo is fresh.... Let's try in that way
iterate over the array
if the sum is zero
    iterate over the array till we reach a positive number
    start a subarray from that element
if the sum is non zero
    add the next element till either the sum becomes zero or array is exhausted
have an anchor variable to keep at the positive number incase the negative unnecessarily decrease the sum
check if the sum is greater than max sum
return max sum
'''


'''
iterate over the array with a cur_sum. max_sum is set to float('-inf')
add the current element to cur_sum
compare with max_sum
check is cur_sum is less than zero
    if true: reassign cur_sum to zero
    else: move on
'''
# Kadane's Algorithm
def max_subarray_sum_one_pass(arr: list) -> int | float:
    max_sum = float('-inf')
    cur_sum = 0

    for num in arr:
        cur_sum += num
        max_sum = max(max_sum, cur_sum)

        if cur_sum < 0:
            cur_sum = 0

    return max_sum


def max_subarray_sum_print_subarray(arr: list) -> list:
    max_sum = float('-inf')
    cur_sum = 0
    start = end = 0

    for i, num in enumerate(arr):
        cur_sum += num

        if cur_sum > max_sum:
            end = i
            max_sum = cur_sum

        if cur_sum < 0:
            cur_sum = 0
            start = i + 1

    return arr[start:end + 1]


run.v8(max_subarray_sum_one_pass)

test_cases = [([[-2, -3, 4, -1, -2, 1, 5, -3]],),
               ([[5,4,-1,7,8]],),
               ([[-2,1,-3,4,-1,2,1,-5,4]], ), 
              ([[3, -100, 4]], )]
run = Engine(test_cases)
run.v8(max_subarray_sum_print_subarray)
        

