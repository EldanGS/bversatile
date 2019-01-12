import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


# Solution 1: O(N) time, O(N) space
def find_smallest_subarray_covering_set1(paragraph, keywords):
    data_keywords = collections.Counter(keywords)
    result = Subarray(-1, -1)
    left, remaining_to_cover = 0, len(keywords)
    for right, word in enumerate(paragraph):
        if word in data_keywords:
            data_keywords[word] -= 1
            if data_keywords[word] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left <= result[1] - result[0]:
                result = (left, right)
            p1 = paragraph[left]
            if p1 in keywords:
                data_keywords[p1] += 1
                if data_keywords[p1] > 0:
                    remaining_to_cover += 1
            left += 1

    return result


# Solution author: no comments
def find_smallest_subarray_covering_set(paragraph, keywords):
    class DoublyLinkedListNode:
        def __init__(self, data=None):
            self.data = data
            self.next = self.prev = None

    class LinkedList:
        def __init__(self):
            self.head = self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def insert_after(self, value):
            node = DoublyLinkedListNode(value)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1

        def remove(self, node):
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            node.next = node.prev = None
            self._size -= 1

    loc = LinkedList()
    d = {s: None for s in keywords}
    result = Subarray(-1, -1)
    for i, s in enumerate(paragraph):
        if s in d:
            it = d[s]
            if it is not None:
                loc.remove(it)
            loc.insert_after(i)
            d[s] = loc.tail

            if len(loc) == len(keywords):
                if result == (-1, -1) \
                        or i - loc.head.data < result[1] - result[0]:
                    result = (loc.head.data, i)

    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "12-6-smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
