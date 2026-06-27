from engine import Engine


'''
About this problem: Split the given array into given k subarrays such that the max subarray sum
is minimum.
'''

test_cases = [([[10, 20, 30, 40], 2], {'ret': 60}), 
              ([[5, 5, 5, 5], 2], {'ret': 10})]
run = Engine(test_cases)

#---Solution-----------------------------------------------------------------------------

'''
Same as the painter's partition problem

return -1 if the len(arr) is less than k

the range of answer is from the max el to the summation of arr.
low at max(arr) and high at sum(arr)

run a while loop with condition low <= high
    calc mid of low and high
    cur_sum = 0
    sub_arr_done = 1

    run a for loop and iterate over arr
        if the sum of cur_sum and arr[i] > mid, this means the current array cannot take this
        number, so we need to give this number to the next subarray.
            increase sub_arr_done by 1
            reset cur_sum and assign it the value of arr[i]

        else, the current subarray can handle the incoming number, sum them
            cur_sum += arr[i]

        if sub_arr_done > k: this means we split the array in more than k parts which means this
        mid cannot be the answer as it required the array to be split in more than k parts.
        another point to note is, more subarrays were used because the capacity of each array was 
        too little, so it needs to be increased.
            break
        
    else, if the for loop ran completely, this means we used less than or equal to k subarrays, this
    could either be the answer or the answer could be smaller, so check the left half
        high = mid - 1
        continue
        
    if the loop broke, the explanation is already given besides the break statement, we need to 
    increase our answer, check the right half of arr
        low = mid + 1

since low starts at a not possible answer and high starts from a possible answer, high will end up
at the last impossible answer and low will end up at the first possible answer. so return low

return low
'''

def solution(arr: list, k: int) -> int:
    if len(arr) < k: 
        return -1
    
    low, high = max(arr), sum(arr)

    while low <= high:
        mid = (low + high) // 2
        sub_arr_done = 1
        cur_sum = 0

        for num in arr:
            if num + cur_sum > mid:
                sub_arr_done += 1
                cur_sum = num
            
            else:
                cur_sum += num
            
            if sub_arr_done > k:
                break

        else:
            high = mid - 1
            continue

        low = mid + 1

    return low


run.v8(solution)