from helpers_function import create_dll, print_list

def reverseDLL(head):
    last = head
    while head:
        last = head.prev
        head.prev, head.next = head.next, last

        head = head.prev

    return last.prev


arr = [1, 2, 3, 4, 5, 6, 7, 8]
head = create_dll(arr)
head = reverseDLL(head)
print_list(head)
