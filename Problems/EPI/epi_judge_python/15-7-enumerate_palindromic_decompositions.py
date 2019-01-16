from test_framework import generic_test


# Solution 1: O(N + 2^N) time, O(2^N) space ?
def palindrome_decompositions(input):
    def directed_palindrome_decompositions(offset, partial_partition):
        if offset == len(input):
            result.append(list(partial_partition))
            return
        for i in range(offset + 1, len(input) + 1):
            prefix = input[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decompositions(i, partial_partition + [prefix])

    result = []
    directed_palindrome_decompositions(0, [])
    return result


# Solution 2: O(N * 2^N) time
def palindrome_decompositions1(text):
    return ([[text[:i]] + right for i in range(1, len(text) + 1)
             if text[:i] == text[:i][::-1]
             for right in palindrome_decompositions(text[i:])]
            or [[]])


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    # print(palindrome_decompositions('0204451881'))
    exit(
        generic_test.generic_test_main(
            "15-7-enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
