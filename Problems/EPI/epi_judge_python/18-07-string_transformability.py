from test_framework import generic_test
import collections, string


# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
    queue = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)

    while queue:
        word = queue.popleft()
        if word.candidate_string == t:
            return word.distance
        for i in range(len(word.candidate_string)):
            for c in string.ascii_lowercase:
                cand = word.candidate_string[:i] + c + word.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    queue.append(StringWithDistance(cand, word.distance + 1))

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("18-07-string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
