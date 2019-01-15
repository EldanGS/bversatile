from test_framework import generic_test, test_utils


# Iterative solution
def generate_power_set(S):
    power_set = [[]]
    for s in S:
        power_set += [item + [s] for item in power_set]

    return power_set


# Recursive solution
def generate_power_set(S):
    power_set = []

    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(S):
            power_set.append(list(selected_so_far))
            # print('\nGet power of set', selected_so_far, to_be_selected)
            return
        # print('Go forward, 1st recursion', to_be_selected)
        directed_power_set(to_be_selected + 1, selected_so_far)
        # print('\nLeft 1st recursion')
        # print('Go forward, 2nd recursion', to_be_selected)
        directed_power_set(to_be_selected + 1, selected_so_far + [S[to_be_selected]])
        # print('\nLeft 2nd recursion', to_be_selected)

    directed_power_set(0, [])
    return power_set


if __name__ == '__main__':
    # S = [0, 1, 2]
    # print(generate_power_set(S))
    exit(
        generic_test.generic_test_main("15-4-power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
