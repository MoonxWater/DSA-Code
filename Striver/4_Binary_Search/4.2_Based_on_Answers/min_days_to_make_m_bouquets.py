from engine import Engine

test_cases = [([[7, 7, 7, 7, 13, 11, 12, 7], 2, 3], {'ret': 12}), 
              ([[1, 10, 3, 10, 2], 3, 2], {'ret': -1}),
              ([[7, 7, 7, 7, 12, 7, 7], 2, 3], {'ret': 12})]
run = Engine(test_cases)


'''
About this problem: return the min number of days required to make m bouquets with k roses, given N number of total roses.
From the array, the ith rose will bloom of the arr[i]th day. If the required number of bouquets are not possible, 
return -1
'''


#---Solution-----------------------------------------------------------------------------

'''
multiply the number of bouquets and the number of roses in each one of them. 
if it is more than len of roses, return -1

assign high to max of roses and low to 1
make min_day 

run a while loop while low <= high
make done_bouquets var
make bouquet var to store roses in current bouquet
calc mid of low and high which will act as the current day

run a for loop inside the while loop using the roses array as range and access its value one by one
if mid  is >= the bloom day of current rose
    add that rose to bouquet and immediately compare the size of bouquet to the req roses in a bouquet.
    if it is less than required size, move on
    else, add 1 to done_bouquets and reassign bouquet to 0
else, if the rose didn't bloom, we have a break in the continuity
    reset bouquet to zero

if done_bouquets == required number of bouquets: we have a candidate
    assign mid to best_day
    high = mid - 1
else, we weren't able to make the required amount of bouquets, maybe too few roses bloomed? up the day!
    low = mid + 1

return best_day (we can also return low as theoretically it will point to the first correct ans which is the best)

'''

def solution(bloom_days: list, req_bouquets: int, req_roses: int) -> int:
    if req_bouquets * req_roses > len(bloom_days):
        return -1
    
    low, high = 1, max(bloom_days)

    while low <= high:
        done_bouquets = 0
        bouquet = 0
        mid = (low + high) // 2

        for day in bloom_days:
            if mid >= day:
                bouquet += 1

                if bouquet == req_roses:
                    done_bouquets += 1
                    bouquet = 0
            else:
                bouquet = 0
        

        if done_bouquets >= req_bouquets:
            high = mid - 1

        else:
            low = mid + 1

    return low


run.v8(solution)    