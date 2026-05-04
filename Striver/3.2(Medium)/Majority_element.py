from engine import Engine

test_cases = [(([2, 2, 3, 3, 1, 2, 2],), 2),
              (([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5],), 5),
              (([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 1, 1, 1, 1],), None)]
run = Engine(test_cases)

'''
Moore's Voting Algorithm
start with the first element and increment the cnt for this element
if you again encounter the same element
if you encounter a different element, decrement the count

if cnt after initialing reaches 0, that part of subarray is cancelled out
move on to the next element right after the subarray.

you will end up with a number that doen't cancel out but to check if majority
run another loop to confirm
'''

def moore_s_voting_algo(arr: list) -> int | None:
    if not arr:
        return
    
    cnt = i = 0
    key = arr[0]

    while i < len(arr):
        if cnt == 0:
            key = arr[i]

        if arr[i] == key:
            cnt += 1
        else:
            cnt -= 1

        i += 1
        
    cnt = 0

    for num in arr:
        if num == key:
            cnt += 1

    return key if cnt > len(arr) // 2 else None


'''
hash all the elements to their cnt
return immediatly if the cnt exceeds n / 2
'''

def majority_element_hash(arr: list) -> int | None:
    freq = {}
    mid = len(arr) // 2

    for num in arr:
        freq[num] = 1 + freq.get(num, 0)
        
        if freq[num] > mid:
            return num
        
    return None


run.v8(majority_element_hash)
run.v8(moore_s_voting_algo)

run.compare(majority_element_hash, moore_s_voting_algo)

