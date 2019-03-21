from test_framework import generic_test, test_utils


def combinations(n, k):
    def directed_combinations(offset, partial_combinations):
        if len(partial_combinations) == k:
            result.append(partial_combinations)
            return

        num_remaining = k - len(partial_combinations)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combinations + [i])
            i += 1

    result = []
    directed_combinations(1, [])
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "15-05-combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
