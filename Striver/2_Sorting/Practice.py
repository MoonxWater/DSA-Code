from engine import Engine


test_cases = [([[5, 5, 8, 4, 2, 1, 9, 8, 0, 7, 5]], {'ret': None})]
run = Engine(test_cases)

# question 1: replicate bubble sort algo

'''
we compare the current element with the next element and see which one is greater
if the current element is greater, swap it with the next one, if not dont

do this for all the el and de
'''

def bubble_sort(arr: list) -> None:
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break


run.v8(bubble_sort)