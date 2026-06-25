from engine import Engine

test_cases = [([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5], {'ret': 15}), 
              ([[5, 4, 5, 2, 3, 4, 5, 6], 5], {'ret': 9}),
              ([[1, 2, 3, 4, 5], 2], {'ret': 9}),
              ([[3,2,2,4,1,4], 3], {'ret': 6})]
run = Engine(test_cases)


'''
About this problem: given an array of item with arr[i] being the weight of the item and given the 
number of days D, return the least capacity required to ship all the items within D days.
'''


#---Solution-----------------------------------------------------------------------------

'''
return 0 if not days or not weights

initialise low and high to max of weights and sum(weights)

run a loop while low <= high
    calc mid of low and high
    make cur_day var = 1
    make container var to store the weights to be transported = 0

    run a for loop and iterate over the weights
        if weight + container > mid: this means we are exceeding capacity 
        so we need to ship the current container and reset its value to the current weight, 
            also wait for one day
        else, everything is within the capacity (even eq), so simply add the weight to the container
        check if the cur_day surpasses the given days, if true: break

    else (for's) if the for loop didn't break, this means we may have a possible answer, but 
    we need the least so high to mid - 1 and continue
    if the for loop broke, this means our capacity is too low, so increase the capacity 
    low = mid + 1

return low
'''

def solution(weights: list, days: int) -> int:
    if not weights or not days:
        return 0
    
    low, high = max(weights), sum(weights)

    while low <= high:
        mid = (low + high) // 2
        cur_day = 1
        container = 0

        for weight in weights:
            if container + weight > mid:
                cur_day += 1
                container = weight

            else:
                container += weight
            
            if cur_day > days:
                break

        else:
            high = mid - 1
            continue

        low = mid + 1

    return low


run.v8(solution)