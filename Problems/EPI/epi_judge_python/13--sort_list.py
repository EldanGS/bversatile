from test_framework import generic_test


class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def merge_two_sorted_lists(L1, L2):
    head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2

    return head.next


def stable_sort_list(L):
    if not L or not L.next:
        return L

    prev_slow, slow, fast = None, L, L
    while fast and fast.next:
        prev_slow = slow
        fast, slow = fast.next.next, slow.next
    prev_slow.next = None

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("13--sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
