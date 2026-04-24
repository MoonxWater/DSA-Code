num = int(input("Enter a number: "))
class Palindrome:
    def is_palindrome(self, num: int) -> bool:
        rev_num = 0
        dup_num = num
        while num > 0:
            rev_num = (rev_num * 10) + (num % 10)
            num = int(num / 10)
        if rev_num == dup_num:
            return True
        return False
check_pal = Palindrome().is_palindrome(num)
print(check_pal)
