from engine import Engine

test_cases = [([[3, 1, -2, -5, 2, -4]], {"mod":[3, -2, 1, -5, 2, -4]})]
run = Engine(test_cases)

'''
About the problem:
The first element is guaranteed to be positive
'''

'''
loop over the array and assign each element to the corresponding position in a new array
keep two variables to look up the next position of insertion
'''
def rearrange_by_sign_optimal(arr: list) -> list:
    p = n = 0
    res = [0] * len(arr)
    
    for i, num in enumerate(arr):
        if num > 0:
            res[2 * p] = num
            p += 1
        else:
            res[2 * n + 1] = num
            n += 1

    return res

# run.v8(rearrang_by_sign_optimal)

'''
create two lists and append pos in one and neg in the other
iterate over the array and insert the values alternatively
'''

def rearrange_by_sign(arr: list) -> None:
    pos = []
    neg = []
    i = k = 0
    is_pos = False

    for j, num in enumerate(arr):
        if num > 0:
            pos.append(num)
            if j == 0:
                is_pos = True
        else:
            neg.append(num)

    while i < len(arr):
        if is_pos:
            arr[i] = pos[k]
            arr[i + 1] = neg[k]
        else:
            arr[i] = neg[k]
            arr[i + 1] = pos[k]
        
        i += 2
        k += 1


def rearrange_by_sign_offset(arr: list) -> None:
    pos_offset = neg_offset = 0
    i = 1
    is_pos = arr[0] > 0

    if arr[0] > 0:
        pos_offset += 1
    else:
        neg_offset += 1

    while i < len(arr):
        if is_pos and arr[i] > 0:
            arr[pos_offset*2], arr[i] = arr[i], arr[pos_offset*2]
            ...
    ...




# run.v8(rearrange_by_sign)

arr = [3, 1, -2, -5, 2, -4]
arr = rearrange_by_sign_optimal(arr)
print(arr)