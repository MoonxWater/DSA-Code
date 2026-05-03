# num = int(input("Enter a number: "))
# i = -1
# while num > 0:
#     digit = num % 10
#     num = int(num / 10)
#     print(f'The digit at index {i} is: {digit}')
#     print(f'Remaining number is: {num}')
#     i -= 1

# num = int(input("Enter a number: "))
# class ReverseNumber:
#     def rev(self, num: int) -> int:
#         rev_num = 0
#         while num > 0:
#             rev_num = (rev_num * 10) + (num % 10)
#             num = int(num / 10)
#         return rev_num
# rev_num = ReverseNumber().rev(num)
# print(rev_num)


# arr = [1, 2, 3]
# ref = arr       # ref points to the same list
# print("ref before:", ref, "ref id:", id(ref))
# print("arr before:", arr, "arr id:", id(arr))
# print(id(ref) == id(arr))
# arr = []        # arr now points to a new empty list
# print("ref after:", ref, "red id:", id(ref))
# print("arr after:", arr, "arr id:", id(arr)) # [1, 2, 3] — ref still sees the old list!
# print(id(ref) == id(arr))


# def n_to_1(n1, n2):
#     if n1 > n2:
#         return
    
#     n_to_1(n1 + 1, n2)
#     print(n1)

# n_to_1(1, 5)

# arr = [1, 2, 3, 4, 5]

# def rev_arr(i = 0):
#     if i >= len(arr) - i - 1: return 

#     arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]

#     rev_arr(i + 1)
    
# rev_arr()
# print(arr)


# def is_palindrome(text, i = 0):
#     if i >= len(text) // 2: return True

#     return (text[i] == text[len(text) - i - 1]) and is_palindrome(text, i + 1)

# text = "abcddcba"
# print(is_palindrome(text))

# def mystery_sort(arr: list):
#     i = 0

#     while i <= len(arr) // 2:
#         for j in range(i, len(arr) - i):
#             print(i, arr, sep=": ")
#             if arr[j] < arr[i]:
#                 print(arr, end=' -> ')
#                 arr[i], arr[j] = arr[j], arr[i]
#                 print(arr)

#             elif arr[j] > arr[len(arr) - i - 1]:
#                 print(arr, end=' -> ')
#                 arr[len(arr) - i - 1], arr[j] = arr[j], arr[len(arr) - i - 1]
#                 print(arr)
        
#         i += 1

#     return arr

# arr = mystery_sort([2, 1, 3])
# print(arr)


# def is_sorted(arr: list) -> bool:
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
    
#     return True

# arr = [2, 4, 4, 6, 7, 8, 10]
# arr2 = [2, 1, 4, 6, 9, 11]
# arr3 = [2, 2, 2, 2, 2, 2, 2, 2]
# arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 0, 9]

# print(is_sorted(arr)) # True
# print(is_sorted(arr2)) # False
# print(is_sorted(arr3)) # True
# print(is_sorted(arr4)) # False



# def topKFrequent(nums: list[int], k: int) -> None:
#     freq = {}

#     for i in range(len(nums)):
#         freq[nums[i]] = 1 + freq.get(nums[i], 0)

#     freq2 = freq.fromkeys(freq.values(), freq.keys())
#     print(freq2)
#     top = []

#     for i in range(k):
#         max(freq.items(), key=lambda x: x[1])

    

# print(topKFrequent([1,2,2,3,3,3, 4], 2))


# def sqrt(num: int) -> int:
#     cur_sum = 0

#     for idx, i in enumerate(range(1, num, 2)):
#         cur_sum += i

#         if cur_sum == num:
#             return idx + 1
    
#     return 0

# print(sqrt(2025))






