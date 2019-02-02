from test_framework import generic_test


class ListNode:
    def __init__(self, data=0, next=None):
        self.data, self.next = data, next


def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2  # L1 if L1 else L2

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("07-01-sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
