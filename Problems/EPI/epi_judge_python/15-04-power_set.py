from test_framework import generic_test, test_utils


def generate_power_set(S):
    def generate_set(to_be_selected, selected_so_far):
        if to_be_selected == len(S):
            power_set.append(selected_so_far)
            return

        generate_set(to_be_selected + 1, selected_so_far)
        generate_set(to_be_selected + 1, selected_so_far + [S[to_be_selected]])

    power_set = []
    generate_set(0, [])

    return power_set


if __name__ == '__main__':
    # generate_power_set([0, 1])
    exit(
        generic_test.generic_test_main("15-04-power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
