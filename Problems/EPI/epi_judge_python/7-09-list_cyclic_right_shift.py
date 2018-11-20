from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    if not L:
        return L

    tail, n, = L, 1
    while tail.next:
        tail = tail.next
        n += 1

    k %= n
    if k == 0:
        return L

    tail.next = L  # cycling list
    new_tail, step_to_new_head = tail, n - k
    while step_to_new_head:
        new_tail = new_tail.next
        step_to_new_head -= 1

    L = new_tail.next
    new_tail.next = None

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("7-09-list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
