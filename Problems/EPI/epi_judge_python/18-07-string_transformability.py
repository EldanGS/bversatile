from test_framework import generic_test
import collections
import string


# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate', 'distance'))
    queue = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)

    while queue:
        word = queue.popleft()

        if word.candidate == t:
            return word.distance

        for i in range(len(word.candidate)):
            for c in string.ascii_lowercase:
                next_candidate = word.candidate[:i] + c + word.candidate[i + 1:]
                if next_candidate in D:
                    queue.append(StringWithDistance(next_candidate, word.distance + 1))
                    D.remove(next_candidate)

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("18-07-string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
