from test_framework import generic_test
import math, bintrees


class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


# Solution 1: O(KlogK) time, O(K) space
def generate_first_k_a_b_sqrt2_1(k):
    candidates = bintrees.RBTree([(Number(0, 0), None)])
    result = []
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)
        candidates[Number(next_smallest.a + 1, next_smallest.b)] = None
        candidates[Number(next_smallest.a, next_smallest.b + 1)] = None

    return result


# Solution 2: O(K) time, O(K) space
def generate_first_k_a_b_sqrt2(k):
    candidates = [Number(0, 0)]
    i = j = 0
    for _ in range(1, k):
        cand_i_plus_1 = Number(candidates[i].a + 1, candidates[i].b)
        cand_j_plus_sqrt2 = Number(candidates[j].a, candidates[j].b + 1)
        candidates.append(min(cand_i_plus_1, cand_j_plus_sqrt2))
        if cand_i_plus_1.val == candidates[-1].val:
            i += 1
        if cand_j_plus_sqrt2.val == candidates[-1].val:
            j += 1

    return [a.val for a in candidates]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("14-7-a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
