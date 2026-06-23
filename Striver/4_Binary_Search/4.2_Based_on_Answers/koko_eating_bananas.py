from engine import Engine

test_cases = [([[25, 23, 4, 10], 4], {'ret': 25}), 
              ([[1, 4, 3, 2], 9], {'ret': 2}),\
                ([[321000000], 998000000], {'ret': 1})]
run = Engine(test_cases)


'''
About this problem: Return an integer k which is the min number of bananas to be eaten by Koko per hr
to finish all the piles within h hrs.
'''


#---Solution-----------------------------------------------------------------------------

'''
make a cur_h to sum eating time
res will store the best answer

get max from the piles list
set low to 1 and high to max
while low <= high, run a loop
calc mid of low and high, floor div
run through the array and div each pile with mid and ceil it.
add the result to cur_h
if at anypoint cur_h exceeds h, break from inner loop
if break, koko too slow, increase speed: low to mid + 1
if did not break, koko either too
fast or perfect: high to mid - 1, res = mid
return res + 1
'''

import math

def solution(piles: list, h: int) -> int:
    low, high = 1, max(piles)
    res = high

    while low <= high:
        mid = (low + high) // 2
        cur_h = 0

        for pile in piles:
            cur_h += math.ceil(pile / mid)

            if cur_h > h:
                break
        else:
            res = mid
            high = mid - 1
            continue
        
        low = mid + 1

    return res


run.v8(solution)