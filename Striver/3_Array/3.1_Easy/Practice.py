from engine import Engine



test_cases_max_consecutive_ones = [([[1, 1, 0, 1, 1, 1, 0, 1, 1]], {'ret':3}),
              ([[0, 1, 1, 0, 1, 1, 1, 0, 1, 1]], {'ret':3})]
max_consecutive_ones_engine = Engine(test_cases_max_consecutive_ones)

# question 1: max consecutive ones

'''
make max_one = float('-inf')
make cur_one = 0

run a loop 0 to n - 1
if arr[i] == 0, compare with max_one and reset cur_one
else, increase cur_one

return max of max_one and cur_one to handle outstanding ones
'''

def max_consecutive_ones1(arr: list) -> int:
    if not arr:
        return -1
    
    max_ones = 0
    cur_ones = 0

    for num in arr:
        if num == 0:
            max_ones = max(max_ones, cur_ones)
            cur_ones = 0
        
        else:
            cur_ones += 1

    return max(max_ones, cur_ones)


# max_consecutive_ones_engine.v8(max_consecutive_ones1)