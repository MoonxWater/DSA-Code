from engine import Engine

'''
About this problem: given a list of coordinates, arrange the given number of cows in such a way
that the min distance between two cows is the max in all possible arrangements.
This means, arrange cows -> get all the dist between the cows -> get the min from this -> arrange
in another way -> get all the dist in this arrangement -> get the min -> do the same for all 
arrangements and find the max of min dist.
'''

test_cases = [([[0, 3, 4, 7, 10, 9], 4], {'ret': 3}), 
              ([[4, 2, 1, 3, 6], 2], {'ret': 5})]
run = Engine(test_cases)

#---Solution-----------------------------------------------------------------------------

'''
sort the pos list.
[0, 3, 4, 7, 9, 10] cows = 4
start by placing cows with 1 dist each, if you are able to place all cows, it might be an answer
increase the distance by 1 and again place all the cows. Do this till you can't place all the cows
at the current value of separation.

The answer will lie in the range [1, max el - min el]
low to 1 and high to last - first

run a loop while low <= high
    calc mid of low and high
    cows_placed = 1
    last_placed = pos[0]
    run a for loop and iterate over the pos array and skip the first el
        if pos[i] - last_placed >= mid: this means we can safely place the cow here
            cows_placed += 1
            last_placed = pos[i]

    if cows_placed < cows: the gap is too big, decrease it
        high = mid - 1
    else, the gap may be fine or too small, increase it
        low = mid + 1

return low

'''

def solution(pos: list, cows: int) -> int:
    if len(pos) < cows:
        return -1
    
    pos.sort()

    low, high = 1, (pos[-1] - pos[0]) // (cows - 1)

    while low <= high:
        mid = (low + high) // 2
        cows_placed = 1
        last_placed = pos[0]

        for i in range(1, len(pos)):
            if pos[i] - last_placed >= mid:
                cows_placed += 1
                last_placed = pos[i]

            if cows_placed >= cows:
                break
        
        else:
            high = mid - 1
            continue

        low = mid + 1

    return high
    

run.v8(solution)