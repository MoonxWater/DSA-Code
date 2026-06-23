from engine import Engine

test_cases = []
run = Engine(test_cases)


from math import log10
num = int(input("Enter a number: "))


class ArmstrongNumber:
    def check_armstrong(self, num: int) -> int:
        dup_num = num
        cube_sum = 0
        dig_len = int((log10(dup_num)) + 1)
        
        while dup_num > 0:
           cube_sum += (dup_num % 10) ** dig_len
           dup_num = int(dup_num / 10) 
        
        return num == cube_sum


check_armstrg = ArmstrongNumber().check_armstrong(num)
print(check_armstrg)