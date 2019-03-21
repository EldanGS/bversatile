from test_framework import generic_test
import math
import bintrees


class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def generate_first_k_a_b_sqrt2(k):
    # Initial for 0 + 0 * sqrt(2)
    candidates = bintrees.RBTree([(Number(0, 0), None)])
    result = []

    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)
        # Adds the next two smallest derived from next_smallest
        candidates[Number(next_smallest.a + 1, next_smallest.b)] = None
        candidates[Number(next_smallest.a, next_smallest.b + 1)] = None

    return result


def generate_first_k_a_b_sqrt2(k):
    cand = [Number(0, 0)]
    i = j = 0
    for _ in range(1, k):
        cand_i_plus_1 = Number(cand[i].a + 1, cand[i].b)
        cand_j_plus_sqrt2 = Number(cand[j].a, cand[j].b + 1)
        cand.append(min(cand_i_plus_1, cand_j_plus_sqrt2))

        if cand_i_plus_1.val == cand[-1].val:
            i += 1
        if cand_j_plus_sqrt2.val == cand[-1].val:
            j += 1

    return [a.val for a in cand]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("14-07-a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
