from test_framework import generic_test


def count_inversions(A):
    def count_subarray_inversions(start, end):
        def merge_sort_and_count_inversions_across_subarray(start, mid, end):
            sorted_A = []
            left_start, right_start, inversion_count = start, mid, 0

            while left_start < mid and right_start < end:
                if A[left_start] <= A[right_start]:
                    sorted_A.append(A[left_start])
                    left_start += 1
                else:
                    inversion_count += mid - left_start
                    sorted_A.append(A[right_start])
                    right_start += 1

            A[start:end] = sorted_A + A[left_start:mid] + A[right_start:end]
            return inversion_count

        if end - start <= 1:
            return 0

        mid = (start + end) // 2
        return (count_subarray_inversions(start, mid) +
                count_subarray_inversions(mid, end) +
                merge_sort_and_count_inversions_across_subarray(start, mid, end))

    return count_subarray_inversions(0, len(A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "24-25-count_inversions.py", 'count_inversions.tsv', count_inversions))
