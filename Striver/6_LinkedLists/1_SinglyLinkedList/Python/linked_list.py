from engine import Engine
from typing import Optional


'''
About this problem: creation of LL
'''

test_cases = [([], {}), 
              ([], {})]
run = Engine(test_cases)


class Node:
    def __init__(self, data, next: Node | None=None):
        self.data = data
        self.next: Optional[Node] = None

class LL:
    @staticmethod
    def convert_arr_to_ll(arr: list) -> Node | None:
        if not arr:
            return None
        
        prev = Node(0)
        head = prev

        for num in arr:
            temp = Node(num)
            prev.next = temp
            prev = temp

        return head.next

    @staticmethod
    def printLL(head: Node | None) -> None:
        if not head:
            return None
        
        while head:
            print(head.data, end=' ')
            head = head.next

x = [2, 4, 6, 8]

head = LL.convert_arr_to_ll(x)

temp = head

while temp:
    print(temp.data, end=' ')
    temp = temp.next

print()

LL.printLL(head)


