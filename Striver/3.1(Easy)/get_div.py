def get_divisors(num: int) -> None:
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            print(i, end=', ')
    print(num)
num = int(input("Enter a number: "))
get_divisors(num)

from math import sqrt
def get_divisors2(num: int) -> list[int]:
    div1 = []
    div2 = []
    i = 1
    while i <= sqrt(num):
        if num % i == 0:
            div1.append(i)
            if i != num/i:
                div2.append(num//i)
        i += 1
    div2.reverse()
    div1.extend(div2)
    return div1

num = int(input("Enter a number: "))
print(get_divisors2(num))