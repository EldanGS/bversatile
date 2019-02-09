from test_framework import generic_test


def reverse_list(head):
    prev = None
    while head:
        head.next, prev, head = (prev, head, head.next)

    return prev


def is_linked_list_a_palindrome(L):
    if not L or not L.next:
        return True

    slow = fast = L
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next

    first_half_iter, second_half_iter = L, reverse_list(slow)
    while first_half_iter and second_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("07-11-is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
