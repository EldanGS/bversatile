from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    def generate_parentheses(num_left_parens_needed,
                             num_right_parens_needed,
                             valid_prefix,
                             result=[]):
        if num_left_parens_needed > 0:
            generate_parentheses(num_left_parens_needed - 1,
                                 num_right_parens_needed,
                                 valid_prefix + '(')

        if num_left_parens_needed < num_right_parens_needed:
            generate_parentheses(num_left_parens_needed,
                                 num_right_parens_needed - 1,
                                 valid_prefix + ')')

        if not num_right_parens_needed:
            result.append(valid_prefix)

        return result

    return generate_parentheses(num_pairs, num_pairs, '')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("15-06-enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
