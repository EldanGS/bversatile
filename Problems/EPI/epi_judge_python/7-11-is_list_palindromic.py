from test_framework import generic_test


def reverse_linked_list(L):
    prev = None
    while L:
        L.next, prev, L = (prev, L, L.next)

    return prev


def is_linked_list_a_palindrome(L):
    if not L:
        return True
    slow = fast = L

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    first_half, second_half = L, reverse_linked_list(slow)
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False

        first_half, second_half = first_half.next, second_half.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("7-11-is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
