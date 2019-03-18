from test_framework import generic_test


def remove_duplicates(L):
    current = L
    while current:
        next_distinct = current.next
        while next_distinct and current.data == next_distinct.data:
            next_distinct = next_distinct.next

        current.next = next_distinct
        current = next_distinct

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "07-08-remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
