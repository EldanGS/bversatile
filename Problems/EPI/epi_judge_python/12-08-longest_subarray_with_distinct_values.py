from test_framework import generic_test


def longest_subarray_with_distinct_entries(A) -> int:
    most_recent_occurrence = {}

    longest_dup_free_subarray_start_index = result = 0
    for i, a in enumerate(A):
        if a in most_recent_occurrence:
            dup_index = most_recent_occurrence[a]

            if dup_index >= longest_dup_free_subarray_start_index:
                result = max(result, i - longest_dup_free_subarray_start_index)
                longest_dup_free_subarray_start_index = dup_index + 1

        most_recent_occurrence[a] = i

    return max(result, len(A) - longest_dup_free_subarray_start_index)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "12-08-longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
