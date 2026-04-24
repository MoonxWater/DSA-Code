from math import log10
num = int(input("Enter a number: "))
class ArmstrongNumber:
    def check_armstrong(self, num: int) -> int:
        dup_num = num
        cube_sum = 0
        dig_len = int((log10(num)) + 1)
        while num > 0:
           cube_sum += (num % 10) ** dig_len
           num = int(num / 10) 
        if dup_num == cube_sum:
            return True
        return False
check_armstrg = ArmstrongNumber().check_armstrong(num)
print(check_armstrg)