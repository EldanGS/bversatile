from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    def helper(num_left_parens_needed, num_right_parens_needed, valid_prefix, result=[]):
        if num_left_parens_needed > 0:
            # print('Go by left parens', num_left_parens_needed)
            helper(num_left_parens_needed - 1, num_right_parens_needed, valid_prefix + '(', result)
        if num_left_parens_needed < num_right_parens_needed:
            # print('\nLeft left parens by valid_prefix:', valid_prefix)
            # print('Go by right parens', num_right_parens_needed)
            helper(num_left_parens_needed, num_right_parens_needed - 1, valid_prefix + ')', result)
            # print('\nLeft right parens')
            # print('Current valid_prefix:', valid_prefix)
        if not num_right_parens_needed:
            # print('\nLeft right parens')
            # print('left, right:', num_left_parens_needed, num_right_parens_needed)
            # print('Current valid_prefix:', valid_prefix)
            result.append(valid_prefix)
        return result

    return helper(num_pairs, num_pairs, '')


if __name__ == '__main__':
    # print(generate_balanced_parentheses(2))
    exit(
        generic_test.generic_test_main("15-6-enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
