def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        idx = i
        for j in range(i - 1, -1, -1):
            if arr[idx] < arr[j]: 
                arr[j], arr[idx] = arr[idx], arr[j] # this is swapping which is expensive as compared to shifting
                idx = j
            
            else: break   

arr = [14, 9, 8, 2, 4, 4, 16, 2]

insertion_sort(arr)
print(arr)