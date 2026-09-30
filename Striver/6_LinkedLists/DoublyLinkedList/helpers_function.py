class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next

def create_dll(arr):
    dummy = Node()
    prev = dummy
    for num in arr:
        temp = Node(num)
        temp.prev = prev
        prev.next = temp
        prev = temp

    dummy = dummy.next
    dummy.prev = None # type: ignore

    return dummy