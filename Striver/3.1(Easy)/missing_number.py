def missing_number(arr: list) -> int:
    '''
    Takes in an array as input
    Loops through the elements of the array and return the first 
    missing number by the condition arr[i] != i + 1
    If all numbers are present, returns -1
    '''

    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
        
    return -1

arr1 = [1, 2, 4, 5]
missing = missing_number(arr1)
print(missing)

def missing_number_logarithmic(arr: list) -> int:
    '''
    Takes an array as input and returns int as output
    1. Calculates the mid of the array and checks whether
        arr[mid] is equal to mid + 1.
        if true: missing element in right half
            low = mid
        else: missing element in left half
            high = mid
    '''
    # Time complexity of O(logn)
    if arr[0] != 1:
        return 1
    
    low = 0
    high = len(arr)
    mid = (low + high) // 2

    while low < mid:
        mid = (low + high) // 2

        if arr[mid] == mid + 1:
            low = mid

        elif arr[mid] == mid + 2:
            if arr[mid - 1] == mid:
                return mid + 1
        
            else:
                high = mid    

    return len(arr) + 1

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40]
missing = missing_number_logarithmic(arr2)
print(missing) # got 39

arr3 = [2, 3, 4, 5, 6]
missing2 = missing_number_logarithmic(arr3)
print(missing2) # got 1

arr4 = [1, 2, 3, 4, 5, 7]
missing3 = missing_number_logarithmic(arr4)
print(missing3) # got 6

arr5 = [1, 3]
print(missing_number_logarithmic(arr5)) # got 2