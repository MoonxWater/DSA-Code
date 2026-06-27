from engine import Engine


'''
About this problem: given an array of area of a wall and the number of painters k, try to minimize
the time it takes for the painter painting the max area and return it. 1 unit area takes 1 unit
time.
'''

test_cases = [([[10, 20, 30, 40], 2], {'ret': 60}), 
              ([[5, 5, 5, 5], 2], {'ret': 10})]
run = Engine(test_cases)

#---Solution-----------------------------------------------------------------------------

'''
Intuition: what is the answer? it is total time taken to paint the wall. what range does this
time belong to? the max of areas array. what is the max possible time to paint the wall?
the sum of areas array. so your range is [max(areas), sum(areas)].

suppose you land at some value in this range, how will you differentiate whether it is correct
or not? i will allocate area to a painter and keep on allocating till the allocated area is 
within the chosen bound. whether this point is correct or not will depend on how many painters it
took to paint the wall for this value.

what happens if you cross this "bound"? i will allocate that area to the next painter.

what if you run out of painters? running out of painters means that each painter is getting too
little area to painter, so i will allocate more area to each painter, this means increasing the
bound.

what if you successfully allocate all the area to all the painters? if i am able to allocate all 
the area to the painters, even if i needed less painters or the perfect amount, in either case, 
i will decrease the area allocated to each painter. this will work even if perfect amount of
painters were used. then will method will look for the best time.
'''

'''
if the length of areas is less than painters, return -1 

since the range is [max(areas), sum(areas)]
low to max(areas) and high to sum(areas)

run a while loop with condition low <= high
    calc mid of low and high
    make done_painters var with initial value 1
    make alc_area = 0

    run a for loop and iterate over the areas array
        if the summation of alc_area and areas[i] > mid, this means the current painter cannot paint
        this area, so we increase the number of painters used and immediately assign this area to
        this new painter

        else, the current painter can handle this area, so add to alc_area

        if at any point in the for loop, the done_painters exceeds given painters, break out of 
        the loop. notice there it is strict > and not =.
    if you did not break out of the for loop, this means either the answer used the perfect amount
    of painters or too few. in both cases, call high to mid - 1, use continue after this

    if you broke out of the for loop, this means each painter was getting too little of an area
    which is indirectly mid, so increase it by low = mid + 1

after the while loop ends, use the zero variable logic to return low as it will point to the ans 
'''

def solution(areas: list, painters: int) -> int:
    if len(areas) < painters:
        return -1 
    
    low, high = max(areas), sum(areas)

    while low <= high:
        mid = (low + high) // 2
        done_painters = 1
        alc_area = 0

        for area in areas:
            if area + alc_area > mid:
                done_painters += 1
                alc_area = area

            else:
                alc_area += area

            if done_painters > painters:
                break

        else:
            high = mid - 1
            continue

        low = mid + 1

    return low

run.v8(solution)
