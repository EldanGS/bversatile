from test_framework import generic_test


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next  # current
    for _ in range(finish - start):
        temp = sublist_iter.next  # next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next,  # next = next-next
                                                           sublist_head.next,  # next-next = next
                                                           temp)  # cur = changed(next)
    return dummy_head.next


if __name__ == '__main__':
    # L = ListNode(11)
    # L.next = ListNode(7)
    # L.next.next = ListNode(5)
    # L.next.next.next = ListNode(3)
    # L.next.next.next.next = ListNode(2)
    # print(reverse_sublist(L, 2, 4))

    exit(
        generic_test.generic_test_main("7-02-reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
