from engine import Engine

test_cases = [([25, 2], {'ret': 4.999999701976776}), 
              ([28, 3], {'ret': 3.036588191986084})]
run = Engine(test_cases)


'''
About this problem: find the nth root of the given number. Accurate to about 5 decimal places.
'''


#---Solution-----------------------------------------------------------------------------

'''
create a funtion that would take a number and multiply it by itself n times.
create the range from 1 to m
create the difference value to make the decimal places accurate and to be used in the loop

assign low to 1 and high to m
run loop while high - low >= 10**(-6): this is the condition that will make the ans accurate to 
5 decimal places
calc mid of low and high but dont use floor division

if the return value of multiply function is greater than m, move high to mid
if the return value is smaller than m, move low to mid

notice how we move it to mid instead of mid + 1 or mid - 1 because we cant add or subtract 1 at every iteration.

for now, lets keep an ans var and return it at last.
'''

def solution(m: int | float, n: int) -> float | int:
    def multiply(num: int | float) -> float | int:
        ans = 1
        for i in range(n):
            ans *= num
        
        return ans
    
    def nth_root() -> float | int:
        ans = -1
        low, high = 0, max(1.0, m)
        acc = 1e-6

        while (high - low) >= acc:
            mid = (low + high) / 2

            midmul = multiply(mid)

            if midmul == m:
                return mid
            
            elif midmul > m:
                high = mid

            else:
                ans = mid
                low = mid
        
        return ans
    
    return nth_root()


run.v8(solution)
