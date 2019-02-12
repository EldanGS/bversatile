from test_framework import generic_test


def can_reach_end(A):
    max_jump, last_index = 0, len(A) - 1
    i = 0
    while i <= max_jump < last_index:
        max_jump = max(max_jump, A[i] + i)
        i += 1

    return max_jump >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "05-04-advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
