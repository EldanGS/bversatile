from test_framework import generic_test


def palindrome_decompositions(input: str) -> []:
    def directed_palindrome_decompositions(offset, partial_partition):
        if offset == len(input):
            result.append(partial_partition)
            return

        for i in range(offset + 1, len(input) + 1):
            prefix = input[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(i, partial_partition + [prefix])

    result = []
    directed_palindrome_decompositions(0, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "15-07-enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
