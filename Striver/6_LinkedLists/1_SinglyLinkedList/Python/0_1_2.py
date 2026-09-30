from helpers_function import create_ll, print_list, Node

def zero_one_two(head):
    zero = Node()
    one = Node()
    two = Node()
    cur = head
    start_zero = zero
    start_one = one

    while cur:
        if cur.val == 2:
            temp = cur
            cur = cur.next
            temp.next = two.next
            two.next = temp
            continue
            
        elif cur.val == 1:
            one.next = cur
            one = one.next
        else:
            zero.next = cur
            zero = zero.next

        cur = cur.next

    zero.next = start_one.next if start_one.next else two.next
    one.next = two.next

    return start_zero.next
    


arr = [1, 0, 2, 1, 1, 0, 2, 0, 0, 2, 2]
head = create_ll(arr)
head = zero_one_two(head)
print_list(head)