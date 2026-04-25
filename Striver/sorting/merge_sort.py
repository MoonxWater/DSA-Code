def merge_sort1(arr: list[int]) -> list[int]:
    if len(arr) <= 1: return arr

    mid = len(arr) // 2

    left = merge_sort1(arr[:mid])
    right = merge_sort1(arr[mid:])

    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1

        else:
            res.append(right[j])
            j += 1            
    
    res.extend(left[i:])
    res.extend(right[j:])

    return res

arr = [3, 1, 1, 4, 7, 2, 4, 7, 9, 0, 6]
print(merge_sort1(arr))

def merge_sort(arr: list[int], low: int, high: int) -> None:
    if low >= high: return

    mid = (high + low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    
    right = mid

    while low < mid:
        if arr[low] > arr[right]:
            arr[low], arr[right] = arr[right], arr[low]        
        low += 1

        
    return

arr = [3, 1, 1, 4, 7, 2, 4, 7, 9, 0, 6]
merge_sort(arr, 0, len(arr))
print(arr)

'''
 l           m                 h
[3, 1, 1, 4, 7, 2, 4, 7, 9, 0, 6]
 l     m     h  l     m        h
[3, 1, 1, 4, 7, 2, 4, 7, 9, 0, 6]
 l  m  h  l  h  l  m  h  l  m  h     
[3, 1, 1, 4, 7, 2, 4, 7, 9, 0, 6]
 l  h  r  r  r  l  h  r  l  h  r 
[3, 1, 1, 4, 7, 2, 4, 7, 9, 0, 6]
 r  r           r  r     r  r   
[3, 1, 1, 4, 7, 2, 4, 7, 9, 0, 6]
                                  
'''

'''
[1, 3, 5 - 2, 4] 1 & 2
[1, 3, 5 - 2, 4] 3 & 2
[1, 2, 5 - 3, 4] 
'''