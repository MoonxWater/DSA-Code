from engine import Engine

test_cases = [([[3, 1, 2]], {'red':[3, 2, 1]})]
run = Engine(test_cases)

''''''

#----Solution----------------------------------------------------------------------------------------------


'''
something to notice, with the base array as 1, 2, 3, if we look at the sum of each perm,
it is something of a pattern -> 9, 81, 18, 81, 9
I will call this as base difference
to calculate the difference between the current perm and the next, the formula is
base difference * difference in digits we are swapping
for example, instead of 123 we had 124, the difference would become
9 * (4 - 2) = 18, so the next perm would be 124 + 18 = 142

'''

def next_perm_obs(arr: list) -> list:
    res = []

    return res

'''
store a sorted ref array.

'''
import math

def next_perm_slope_rotate(arr: list) -> list:
    ref = sorted(arr)
    sat = False
    ret_flag = False

    for i in range(math.factorial(len(arr)) - 1):
        print(ref)
        if ret_flag:
            print("ref:", ref)
            return ref

        if sat:
            ref[-3], ref[-2] = ref[-2], ref[-3]
            sat = False
        else:
            ref[-2], ref[-1] = ref[-1], ref[-2] 
            sat = True
        
        if ref == arr:
            ret_flag = True
        
    ref.reverse
    print("hello")
    return ref

print(next_perm_slope_rotate([3, 2, 1]))


'''
brute force, generate all perms
look for the arr in the list
return the next. if arr is last, return first
'''