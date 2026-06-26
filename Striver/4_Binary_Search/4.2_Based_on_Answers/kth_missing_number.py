from engine import Engine

test_cases = [([[2, 3, 4, 7, 11], 5], {'ret': 9}),
              ([[4, 7, 9, 10], 4], {'ret': 5})]
run = Engine(test_cases)


'''
About this problem: given an array and a number k, return the kth 
number missing from the array. For example, [2, 3, 5, 6] and k = 2,
 the kth number missing is 4.
'''


#---Solution-----------------------------------------------------------------------------

'''
if vec is empty, return 1
if the last el in vec is = to the len(vec), return last el + k

this is not a obvious binary search, we implement we need to get the two indices where the 
answer lies. for example, in the array [2, 3, 4, 7, 11] with k = 5, the answer lies b/w 7 & 11 with 
indices 3 and 4.
To get this, we need low and high to 0 and len(vec) - 1

run a loop while low <= high
    calc mid of low and high
    
    check the el at mid
    if vec[mid] - mid - 1 >= k: this means that before this index, there are this much number of
    missing els. if that number is >= k, we need dont need to check the right half.
        eliminate the right half
    else, eliminate the left half

after the while loop, low and high will point at those indices with low at the right boundary and
high at the left boundary.

to get the missing number, we get the total missing numbers till index high and subtract this number
with k. the result will give us the offset we need to go after high and before low to reach the 
answer. add this result to the el at high
vec[high] + (k - (vec[high] - high - 1))
vec[high] + (k - vec[high] + high + 1)
vec[high] + k - vec[high] + high + 1
k + high + 1
since high + 1 = low
result = low + k
return the result
'''

def solution(vec: list, k: int) -> int:
    if not vec:
        return 1
    
    if vec[-1] == len(vec):
        return vec[-1] + k

    low, high = 0, len(vec) - 1
    
    while low <= high:
        mid = (low + high) // 2


        if vec[mid] - mid - 1 >= k:

            high = mid - 1

        else:

            low = mid + 1

    return low + k


run.v8(solution)

