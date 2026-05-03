'''
checks if len of array is equal to len of set of array. return immediatly if true

iterate over the array (considering it is sorted), the loop goes from 1 to n - 1 
if the current element is equal
to the prev element, remove current element. But after removal, the length of the 
array we are traversing is compromised, so we store an offset variable
increment offset whenever we remove an element.
use offset in calculation of index for the current and prev element
'''


def remove_dup(arr: list) -> None:
    if len(arr) == len(set(arr)):
        return
    
    offset = 0

    for i in range(1, len(arr)):
        if arr[i - offset] == arr[i - 1 - offset]:
            arr.pop(i - offset)
            offset += 1
    

arr = [1, 1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 9, 9]
remove_dup(arr)
print(arr)