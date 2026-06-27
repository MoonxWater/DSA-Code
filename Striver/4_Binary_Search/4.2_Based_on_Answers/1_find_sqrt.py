from engine import Engine

test_cases = [([28], {'ret': 5}), 
              ([25], {'ret': 5}),
              ([89], {'ret': 9})]
run = Engine(test_cases)


'''
About this problem: Find the sqrt of the given number in O(logn)
'''


#---Solution-----------------------------------------------------------------------------

'''
low to 1 and high to the given number
while low <= high
calc mid of low and high
calc mid * mid
if midsq is greater than number, eliminate the right half
if midsq is smaller than the number, eliminate the left half and store it as possible answer
'''

def solution(n: int) -> int:
    low, high = 1, n
    ans = 1

    while low <= high:
        mid = (low + high) // 2

        midsq = mid * mid

        if midsq == n:
            return mid
        
        elif midsq > n:
            high = mid - 1
        
        else:
            ans = mid
            low = mid + 1

    return ans


def sqrt(num: int) -> int:
    cur_sum = 0

    for idx, i in enumerate(range(1, num, 2)):
        cur_sum += i

        if cur_sum == num:
            return idx + 1
    
    return 0


run.v8(solution)

print(sqrt(2025))