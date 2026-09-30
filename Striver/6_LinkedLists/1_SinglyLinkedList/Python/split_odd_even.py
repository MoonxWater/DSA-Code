from helpers_function import print_list, Node, create_ll

def split_odd_even(head):
    odd_dummy = Node()
    odd_prev = odd_dummy
    even_dummy = Node()
    even_prev = even_dummy
    cnt = 1

    while head:
        temp = Node(head.val)
        
        if cnt % 2:
            odd_prev.next = temp
            odd_prev = temp

        else:
            even_prev.next = temp
            even_prev = temp

        cnt += 1
        head = head.next

    odd_prev.next = even_dummy.next

    return odd_dummy.next

def split_odd_even_2(head):
    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd, even = odd.next, even.next

    odd.next = even_head
    return head

arr = [1, 2, 3, 4, 5, 6, 7]
head = create_ll(arr)
head2 = create_ll(arr)
head = split_odd_even(head)
head2 = split_odd_even_2(head2)
print_list(head)
print()
print_list(head2)

    
    