from test_framework import generic_test


def can_reach_end(A):
    max_jump, n = 0, len(A) - 1

    i = 0
    while i <= max_jump and max_jump < n:
        max_jump = max(max_jump, i + A[i])
        i += 1

    return max_jump >= n


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
