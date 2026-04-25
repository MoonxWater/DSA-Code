def union(arr1: list, arr2: list) -> list:
    i = j = 0
    res = set()

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.add(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            res.add(arr2[j])
            j += 1
        else:
            res.add(arr1[i])
            i += 1
            j += 1
    
    res.update(arr1[i:])
    res.update(arr2[j:])

    return sorted(res)

arr1 = [1, 1, 2, 3, 4, 5, 7]
arr2 = [2, 3, 4, 4, 5, 6, 10, 11, 12, 12]

res = union(arr1, arr2)
print(res)


def intersection(arr1: list, arr2: list) -> list:    
    i = j = 0
    res = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        
        elif arr1[i] > arr2[j]:
            j += 1

        else:
            i += 1

    return res

arr1 = [1, 1, 2, 3, 4, 5, 7]
arr2 = [1, 1, 2, 3, 4, 4, 5, 6, 10, 11, 12, 12]

res = intersection(arr1, arr2)
print(res)

arr1 = []
arr2 = [2, 3, 4, 4, 5, 6]

res = intersection(arr2, arr1)
print(res)