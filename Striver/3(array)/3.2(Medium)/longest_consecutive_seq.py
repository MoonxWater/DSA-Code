from engine import Engine

test_cases = [([[102, 4, 100, 1, 101, 3, 2, 1, 1, 103, 104, 103]], {'ret':5})]
run = Engine(test_cases)

'''
About this problem:
'''


#----Solution----------------------------------------------------------------------


'''
1. sort the array
2. if arr[i] + 1 = arr[i + 1], increment length
3. drop all elements that are same so that we don't include them in the sequence
4. check if length is greater than max length
5. return max length after finally comparing with length for trailing sequence
'''

def longest_consecutive_sequence_sort(arr: list[int]) -> int:
    if not arr:
        return 0
    
    dup = sorted(arr)
    max_length = length = 1

    for i in range(len(dup) - 1):
        if dup[i] + 1 == dup[i + 1]:
            length += 1
        
        elif dup[i] < dup[i + 1]:
            max_length = max(length, max_length)
            length = 1

    return max(length, max_length)


run.v8(longest_consecutive_sequence_sort)
