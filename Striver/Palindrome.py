from engine import Engine

test_cases = [([1023201], {'ret': True}),
              ([12345], {'ret':False})]
run = Engine(test_cases)

'''
About this problem:
'''

# ----Solutions---------------------------------------------------------


'''
store two variables rev num and dup num
rev num -> 0 and dup num -> num
1. extract the last digit of dup num by the % operator and add it
    to rev num + (rev num * 10)(shift what was prev stored in rev num by one place left)
2. since the last digit was extracted, remove it by dividing dup num by 10 (//)
3. return rev num == num
'''

def is_palindrome(num: int) -> bool:
    rev_num = 0
    dup_num = num

    while dup_num > 0:
        rev_num = (rev_num * 10) + (dup_num % 10)
        dup_num = dup_num // 10

    return rev_num == num


'''
two pointer at both ends
store a num string
1. check equality of el at both pointers
2. if !=, return False
3. if equal, increment l and decrement r
4. loop will go on till l < r
5. return True if not False was returned
'''

def is_palindrome_two_pointer(num: int) -> bool:
    num_str = str(num)
    l , r = 0, len(num_str) - 1

    while l < r:
        if num_str[l] != num_str[r]:
            return False
        
        l += 1
        r -= 1

    return True


'''

'''

def is_palindrome_text_recurse(text: str, i: int = 0) -> bool:
    if i >= len(text) // 2: return True

    return (text[i] == text[len(text) - i - 1]) and is_palindrome_text_recurse(text, i + 1)

text = "abcddcba"
print(is_palindrome_text_recurse(text))


run.v8(is_palindrome)
run.v8(is_palindrome_two_pointer)

run.compare(is_palindrome, is_palindrome_two_pointer)