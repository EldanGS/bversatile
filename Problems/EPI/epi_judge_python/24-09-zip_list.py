from test_framework import generic_test


def reverse_list(head):
    reversed_head = None
    while head:
        head.next, reversed_head, head = (reversed_head, head, head.next)

    return reversed_head


def zipping_linked_list(L):
    if not L or not L.next:
        return L

    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    first_half_head = L
    second_half_head = slow.next
    slow.next = None
    second_half_head = reverse_list(second_half_head)

    first_half_iter, second_half_iter = first_half_head, second_half_head
    while second_half_iter:
        second_half_iter.next, first_half_iter.next, second_half_iter = (
            first_half_iter.next, second_half_iter, second_half_iter.next
        )
        first_half_iter = first_half_iter.next.next

    return first_half_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-09-zip_list.py", 'zip_list.tsv',
                                       zipping_linked_list))
