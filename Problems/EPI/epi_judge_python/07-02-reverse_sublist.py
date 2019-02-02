from test_framework import generic_test


class ListNode:
    def __init__(self, data=0, next=None):
        self.data, self.next = data, next


def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_it = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_it.next
        sublist_it.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("07-02-reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
