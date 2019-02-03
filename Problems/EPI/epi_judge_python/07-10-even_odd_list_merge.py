from test_framework import generic_test


class ListNode:
    def __init__(self, data=0, next=None):
        self.data, self.next = data, next


def even_odd_merge(L):
    if not L:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1

    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("07-10-even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
