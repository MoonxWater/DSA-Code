from engine import Engine


'''
About this problem: 
'''

test_cases = [([], {}), 
              ([], {})]
run = Engine(test_cases)

#---Solution-----------------------------------------------------------------------------

'''

'''

def second_order(arr: list) -> list[float]:
    def second_largest() -> float:
        largest = float('-inf')
        s_largest = float('-inf')

        for i in range(len(arr)):
            if arr[i] > largest:
                s_largest = largest
                largest = arr[i]

            elif largest > arr[i] > s_largest:
                s_largest = arr[i]
        
        return s_largest


    def second_smallest() -> float:
        smallest = float('inf')
        s_smallest = float('inf')

        for i in range(len(arr)):
            if arr[i] < smallest:
                s_smallest = smallest
                smallest = arr[i]
            
            elif smallest < arr[i] < s_smallest:
                s_smallest = arr[i]
        
        return s_smallest
    return [second_smallest(), second_largest()]

    

arr = [0, 2, 4, 1, 10, 5, 7, 9, 15]
test_arr = [2, 1]
test_arr2 = [1, 1, 1, 1, 1]

print(second_order(arr))

print(second_order(test_arr))

print(second_order(test_arr2))


def second_order2(arr: list) -> list[float]:
    def second_largest() -> float:
        largest = float('-inf')
        s_largest = float('-inf')

        for num in arr:
            if num > largest:
                s_largest = largest
                largest = num
            elif largest > num > s_largest:
                s_largest = num

        return s_largest

    def second_smallest() -> float:
        smallest = float('inf')
        s_smallest = float('inf')

        for num in arr:
            if num < smallest:
                s_smallest = smallest
                smallest = num
            elif smallest < num < s_smallest:
                s_smallest = num

        return s_smallest

    return [second_smallest(), second_largest()]

# Test cases 
arr1 = [0, 2, 4, 1, 10, 5, 7, 9, 15]
arr2 = [2, 1]
test_arr2 = [1, 1, 1, 1, 1]

print(second_order2(arr1)) 
print(second_order2(arr2)) 
print(second_order2(test_arr2))
