from engine import Engine

test_cases = [([[3, 1, 2]], {'red':[3, 2, 1]}),
              ([[2, 1, 5, 4, 3, 0, 0]], {'ret':[2, 3, 0, 0, 1, 4, 5]})]
run = Engine(test_cases)

'''
About this Problem:
return the next perm order wise.
if the given array is last in perm order, return first perm
'''

#----Solution----------------------------------------------------------------------------------------------


'''
longest prefix match approach; ex: [2, 1, 5, 4, 3, 0, 0] 
1. look for break point where slope dips ie in the example array, dip is between 1 and 5
2. look from back the first element which is greater than element at breakpoint and swap them
    [2, 3, 5, 4, 1, 0, 0]
3. reverse the array from breakpoint + 1 to end
    [2, 3, 0, 0, 1, 4, 5] <- This is the answer
'''

def next_perm_prefix(arr: list[int]) -> list[int]:
    brk_pt_idx = -1
    ret = arr.copy()
    
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            brk_pt_idx = i - 1
            break
    if brk_pt_idx == -1:
        ret.reverse()
        return ret
    
    for i in range(len(arr) - 1, brk_pt_idx, -1):
        if ret[i] > ret[brk_pt_idx]:
            ret[i], ret[brk_pt_idx] = ret[brk_pt_idx], ret[i]
            break
    
    ret[brk_pt_idx+1:] = ret[:brk_pt_idx:-1]

    return ret



'''
something to notice, with the base array as 1, 2, 3, if we look at the sum of each perm,
it is something of a pattern -> 9, 81, 18, 81, 9
I will call this as base difference
to calculate the difference between the current perm and the next, the formula is
base difference * difference in digits we are swapping
for example, instead of 123 we had 124, the difference would become
9 * (4 - 2) = 18, so the next perm would be 124 + 18 = 142

'''

def next_perm_obsrv(arr: list) -> list:
    res = []

    return res


run.v8(next_perm_prefix)