from test_framework import generic_test


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    if not L:
        raise ValueError('List does not exist')

    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        if not first:
            raise IndexError('Length of given List less than K')

        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next

    second.next = second.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("07-07-delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
