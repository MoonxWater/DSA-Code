from engine import Engine

test_cases = [([[10, 22, 12, 3, 0, 6]], {'ret':[6, 12, 22]}),
              ([[4, 7, 3, 4, 0, 2, 1, 0, -1, -5, -9, -15]], {'ret':[-15, -9, -5, -1, 0, 1, 2, 4, 7]})
              ]
run = Engine(test_cases)

'''
About this problem:
if everything on the right of the element is smaller, it is a leader
return all leaders
the last element will always be a leader
'''


#---Solution-----------------------------------------------------------------------------------


'''
iterate in rev order from the second last element
keep a max var to store the greatest element seen so far
keep a leaders array to store leaders

if current element is greater than max: add cur el to leaders and update max to cur el

if list order matters, return reversed ans list
'''

def leaders_in_an_array_one_pass(arr: list[int]) -> list[int]:
    if not arr: 
        return []
    
    leaders = [arr[-1]]
    max_el = arr[-1]

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_el:
            leaders.append(arr[i])
            max_el = arr[i]

    return leaders


'''
Brute force approach
take each element and check every other element on the right
if taken element is max by the end of the loop, it is a leader
'''

def leader_brute_force(arr: list):
    leaders = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                break
        else:
            leaders.append(arr[i])

    leaders.reverse()
    
    return leaders

run.v8(leaders_in_an_array_one_pass)
run.v8(leader_brute_force)

run.compare(leader_brute_force, leaders_in_an_array_one_pass)