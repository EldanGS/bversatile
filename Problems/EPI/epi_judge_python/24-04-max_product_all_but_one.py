from test_framework import generic_test


def find_biggest_n_minus_one_product(A):
    number_of_negatives = 0
    least_nonnegative_idx = least_negative_idx = greatest_negative_idx = None

    for i, a in enumerate(A):
        if a < 0:
            number_of_negatives += 1
            if least_negative_idx is None or A[least_negative_idx] < a:
                least_negative_idx = i
            if greatest_negative_idx is None or A[greatest_negative_idx] > a:
                greatest_negative_idx = i
        else:
            if least_nonnegative_idx is None or A[least_nonnegative_idx] > a:
                least_nonnegative_idx = i

    idx_to_skip = (least_negative_idx
                   if number_of_negatives & 1 else least_nonnegative_idx
                   if least_nonnegative_idx is not None else greatest_negative_idx)

    max_product = 1
    for i, a in enumerate(A):
        if i != idx_to_skip:
            max_product *= a

    return max_product


if __name__ == '__main__':
    # print(find_biggest_n_minus_one_product([-1, -2, -3, -4, -5]))
    exit(
        generic_test.generic_test_main("24-04-max_product_all_but_one.py",
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
