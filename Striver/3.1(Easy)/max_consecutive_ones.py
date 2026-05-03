'''
input = [1, 1, 0, 1, 1, 1, 0, 1, 1]
output = 3
'''

'''
one variable to store max ones
one variable to store current ones

at zero, compare cur one with max one
and reset cur one

return max one
'''

def max_consecutive_ones1(arr: list) -> int:
    max_ones = cur_ones = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            cur_ones += 1
        
        else:
            max_ones = max(cur_ones, max_ones)
            cur_ones = 0

    return max(max_ones, cur_ones)
    

arr = [0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
print(max_consecutive_ones1(arr))


'''
instead of incrementing cnt by 1 when the loop encounters
1, i will look up for 0 and check the current index i - last
index at which 0 was found - 1 (because in between)
'''

def max_consecutive_ones2(arr: list) -> int:
    max_ones = idx = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            max_ones = max(i - idx - 1, max_ones)
            idx = i

    return max(max_ones, len(arr) - idx - 1)
    

arr = [0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
print(max_consecutive_ones2(arr))