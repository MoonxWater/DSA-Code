from engine import Engine

test_cases = []
run = Engine(test_cases)

'''
We have to return all the divisors of a given number
'''

#----Solution-------------------------------------------------------------------------------------

'''
#We will use the sqrt optimisation
#every divisor would require another divisor to be multiplied with to get
the target number
#by the time we reach the sqrt of the number, we would have seen all the divisors
#loop from 1 to sqrt(num) + 1
#if index completly divides number, add index to a list
#within the same if statement, check if number/index != index (incase perfect square)
#if not, add number/index to another list
#return list1 + reversed(list2)
'''

from math import sqrt
def get_divisors_sqrt_opt(num: int) -> list[int]:
    div1 = []
    div2 = []
    lim = sqrt(num)
    i = 1
    while i <= lim:
        if num % i == 0:
            div1.append(i)
            if i != num/i:
                div2.append(num//i)
        i += 1
    div2.reverse()

    return div1 + div2

num = int(input("Enter a number: "))
print(get_divisors_sqrt_opt(num))



'''
iterate from 1 to n // 2 + 1
if the current index completly divides given number, it is a divisor
print the index
'''
def get_divisors_half_no_space(num: int) -> None:
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            print(i, end=', ')
    print(num)


num = int(input("Enter a number: "))
get_divisors_half_no_space(num)